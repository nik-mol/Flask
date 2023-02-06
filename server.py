from flask import Flask, jsonify, request
from flask.views import MethodView
from sqlalchemy.exc import IntegrityError

from database import AdvertisementModel, Session
from errors import HttpExeption
from schema import (CreateAdvertisementSchema, PutchAdvertisementSchema,
                    validate)

app = Flask("app")


@app.errorhandler(HttpExeption)
def error_handler(error: HttpExeption):
    http_response = jsonify({"status": "error", "message": error.message})
    http_response.status_code = error.status_code

    return http_response


def get_advertisement(advertisement_id: int, session: Session) -> AdvertisementModel:
    advertisement = session.query(AdvertisementModel).get(advertisement_id)
    if advertisement is None:
        raise HttpExeption(status_code=404, message="advertisement nod found")
    return advertisement


class Advertisement(MethodView):
    def get(self, advertisement_id: int):
        with Session() as session:
            advertisement = get_advertisement(advertisement_id, session)
            return jsonify(
                {
                    "id": advertisement_id,
                    "title": advertisement.title,
                    "creation": advertisement.create_time.isoformat(),
                    "owner": advertisement.owner,
                }
            )

    def patch(self, advertisement_id: int):
        json_data = validate(request.json, PutchAdvertisementSchema)
        with Session() as session:
            advertisement = get_advertisement(advertisement_id, session)
            for field, value in json_data.items():
                setattr(advertisement, field, value)
            session.add(advertisement)
            session.commit()
            return jsonify({"status": "success"})

    def post(self):
        advertisement_data = validate(request.json, CreateAdvertisementSchema)
        with Session() as session:
            new_advertisement = AdvertisementModel(**advertisement_data)
            session.add(new_advertisement)
            try:
                session.commit()
            except IntegrityError:
                raise HttpExeption(409, "title alredy exists")
            return jsonify({"id": new_advertisement.id})

    def delete(self, advertisement_id: int):
        with Session() as session:
            advertisement = get_advertisement(advertisement_id, session)
            session.delete(advertisement)
            session.commit()
            return jsonify({"status": "success"})


app.add_url_rule(
    "/advertisements/<int:advertisement_id>",
    view_func=Advertisement.as_view("advertisements"),
    methods=["GET", "PATCH", "DELETE"],
)
app.add_url_rule(
    "/advertisements/",
    view_func=Advertisement.as_view("create_advertisement"),
    methods=["POST"],
)

if __name__ == "__main__":
    app.run()
