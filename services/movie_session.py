from db.models import MovieSession
import datetime


def create_movie_session(movie_show_time: datetime.datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    return MovieSession.objects.create(show_time=movie_show_time,
                                       cinema_hall_id=cinema_hall_id,
                                       movie_id=movie_id)


def get_movies_sessions(session_date: str = None) -> list[MovieSession]:
    if session_date:
        return list(MovieSession.objects.filter(show_time__date=session_date))
    return list(MovieSession.objects.all())


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.filter(id=movie_session_id).first()


def update_movie_session(session_id: int,
                         show_time: datetime.datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> MovieSession:
    session = get_movie_session_by_id(session_id)

    if session:
        if show_time is not None:
            session.show_time = show_time
        if movie_id is not None:
            session.movie_id = movie_id
        if cinema_hall_id is not None:
            session.cinema_hall_id = cinema_hall_id
        session.save()

    return session


def delete_movie_session_by_id(session_id: int) -> MovieSession:
    session = get_movie_session_by_id(session_id)
    if session:
        session.delete()
    return session
