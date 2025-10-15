/*테이블 생성*/
CREATE TABLE juso(
       seq integer primary key autoincrement, 
       name char(20), 
       address char(200)
);

/*테이블 삭제*/
drop table juso;

/*데이터(행) 입력*/
insert into juso(name, address) values('홍길동', '인천서구 경서동');
insert into juso(name, address) values('심청이', '경기도 광명시');

/*데이터 확인*/
select * from juso;
select name from juso where name like '%동' order by name desc;
select * from juso order by address desc;

/*데이터(행) 삭제*/
delete from juso where seq = 1;

/*데이터 수정*/
update juso set name='김길동', address='서울시 강남구 압구정동' where seq = 1;