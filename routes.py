from flask import request, jsonify
from config import db
from models import Episode, Guest, Appearance

def register_routes(app):

    # ---------------- GET /episodes ----------------
    @app.route("/episodes", methods=["GET"])
    def get_episodes():
        episodes = Episode.query.all()
        return jsonify([e.to_dict(only=("id", "date", "number")) for e in episodes])


    # ---------------- GET /episodes/:id ----------------
    @app.route("/episodes/<int:id>", methods=["GET"])
    def get_episode(id):
        episode = Episode.query.get(id)

        if not episode:
            return jsonify({"error": "Episode not found"}), 404

        return jsonify(episode.to_dict(
            include={"appearances": {"include": {"guest"}}}
        ))


    # ---------------- GET /guests ----------------
    @app.route("/guests", methods=["GET"])
    def get_guests():
        guests = Guest.query.all()
        return jsonify([g.to_dict() for g in guests])


    # ---------------- POST /appearances ----------------
    @app.route("/appearances", methods=["POST"])
    def create_appearance():
        data = request.get_json()

        try:
            appearance = Appearance(
                rating=data["rating"],
                episode_id=data["episode_id"],
                guest_id=data["guest_id"]
            )

            db.session.add(appearance)
            db.session.commit()

            return jsonify(appearance.to_dict(
                include=("episode", "guest")
            )), 201

        except Exception as e:
            return jsonify({"errors": [str(e)]}), 400
