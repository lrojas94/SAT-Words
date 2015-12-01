$(function(){
	$('font').each(function(index,elem){
    	if($(elem).attr('color')){
        	$(elem).remove();
        }
    });
		
    function strip(html)
    {
       var tmp = document.createElement("DIV");
       tmp.innerHTML = html;
       return tmp.textContent || tmp.innerText || "";
    }

    var arr = $('p').html().split('<br>');
    var reg = /(\w+[-\w]+|\w+[\s\w]+)\s(\w+\.)\s(.*)/
    var final = [];

    for(var i = 0; i < arr.length;i++){
    	var w = strip(arr[i]);
        w = w.trim();
        w = w.match(reg);
        var res = {};
        if(w == null){
        	console.log(arr[i]);
        }
        res['word'] = w[1];
        res['type'] = w[2];
        res['definition'] = w[3];

        final.push(res);
    }

    console.log(JSON.stringify(final));
})
