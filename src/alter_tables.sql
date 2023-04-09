-- primary for movie
alter table [dbo].[movie] add constraint movie_pk primary key (id);
-- primary for genre
alter table [dbo].[genre] add constraint genre_pk primary key (id);
-- primary for productionCompary
alter table [dbo].[productioncompany] add constraint productioncompany_pk primary key (id);
-- primary for collection
alter table [dbo].[collection] add constraint collection_pk primary key (id);
-- primary for movieCast
alter table [dbo].[movie_cast] add constraint movie_cast_pk primary key (cid, movie_id, person_id);
-- primary for movieCrew
alter table [dbo].[movie_cast] add constraint movie_crew_pk primary key (cid, movie_id, person_id);
-- primary for keyword
alter table [dbo].[keyword] add constraint keyword_pk primary key (id);

-- foreign for belongsToCollection
alter table [dbo].[belongsTocollection] add constraint fk_movieid foreign key (movie_id) references movie(id);
alter table [dbo].[belongsTocollection] add constraint fk_collectionid foreign key (collection_id) references collection(id)
-- foreign for hasGenre
alter table [dbo].[hasGenre] add constraint fk_movieid_hasGenre foreign key (movie_id) references movie(id);
alter table [dbo].[hasGenre] add constraint fk_genreid foreign key (genre_id) references genre(id);
-- foreign for hasProductionCompany
alter table [dbo].[hasProductioncompany] add constraint fk_movieid_hasProductioncomany foreign key (movie_id) references movie(id);
alter table [dbo].[hasProductioncompany] add constraint fk_pcid foreign key (pc_id) references productioncompany(id);
-- foreign for ratings
alter table [dbo].[ratings] add constraint fk_movieid_ratings foreign key (movie_id) references movie(id);
-- foreign for movieCast
alter table [dbo].[movie_cast] add constraint fk_movieid_moviecast foreign key (movie_id) references movie(id);
-- foreign for movieCrew
alter table [dbo].[movie_crew] add constraint fk_movieid_moviecrew foreign key (movie_id) references movie(id);
-- foreign for hasKeyword
alter table [dbo].[hasKeyword] add constraint fk_movieid_haskeyword foreign key (movie_id) references movie(id);
alter table [dbo].[hasKeyword] add constraint fk_keywordid foreign key (keyword_id) references keyword(id);
