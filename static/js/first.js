$(document).ready(function(){


    
    $("#focusedInput").keydown(function(e){
        if(e.keyCode==13){
            var user = $('#focusedInput').val();
            /u\/(\d+)/.test(user);
            user = RegExp.$1;
            if (user==''){
                alert('格式错误！');
                return 0;
            }

            $.get('/verify',{username:user} ,function(data, status){
                if (data['do_exist']=='False'){
                    domain = document.domain
                    if (domain=='localhost'){
                        domain = domain + ':81';
                    }
                    window.location.href='http://' + domain + '/second';

                }
                else {
                    alert('嘤嘤嘤，机器人已经自动为你同步咯！无需再次登陆~~');
                }
            })
        }
    })

    $("button").click(function(){
        var user = $('#focusedInput').val();
        /u\/(\d+)/.test(user);
        user = RegExp.$1;
        if (user==''){
            alert('格式错误！');
            return 0;
        }

        $.get('/verify',{username:user} ,function(data, status){
            if (data['do_exist']=='False'){
                domain = document.domain
                if (domain=='localhost'){
                    domain = domain + ':81';
                }
                window.location.href='http://' + domain + '/second' ;

            }
            else {
                alert('嘤嘤嘤，机器人已经自动为你同步咯！无需再次登陆~~');
            }
        })
});
});