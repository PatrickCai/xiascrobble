$(document).ready(function(){
    $("button").click(function(){
            domain = document.domain
            if (domain=='localhost'){
                domain = domain + ':81';
            }
            window.location.href='http://' + domain + '/first';
});
});