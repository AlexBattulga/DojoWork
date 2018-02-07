$(document).ready(function(){
    $(document).on('click', 'img', function(){
        var id = this.id;
        $.get("https://www.anapioficeandfire.com/api/houses/" + id, function(res){
            var html = "";
            html += "<p>Name: " + res['name'] + "</p>";
            html += "<p>Words: " + res['words'] + "</p>";
            html += "<div class='title'>";
            html += "<p id='title'>Title: " + res['titles'] + "</p>";
            html += "</div>";
            $('.content').html(html);
        })
    })
});
