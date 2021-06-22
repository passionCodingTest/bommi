<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
 
<p>time : <span id="time"></span></p>
 
<form>
    <input type="hidden" value="Ajax_test" name="topic" />
    
    <select name="timezone">
        <option value="Asia/Seoul">asia/seoul</option>
        <option value="America/New_York">America/New_York</option>
    </select>
    
    <select name="format">
        <option value="hh:mm:ss">시/분/초 </option>
        <option value="hh:mm">시간 / 분</option>
        <option value="hh">시간</option>
    </select>
 
</form>
 
<input type="button" value="실행하기" id="execute"/>
 
 
<script src="//code.jquery.com/jquery-1.11.0.min.js"></script>
 
<script>
    $('#execute').click(function(){
        $.ajax({
            url:'testServer.jsp', //통신할 서버 페이지
            type:'post', //기본형식은 get post면 따로 써주기
            //form에 잇는 데이터를 name:value 값으로 매칭시켜보내줌
            data:$('form').serialize(), 
            success:function(data){
                $('#time').text(data); //받아온 data 실행
            }
        })
    })
</script>
