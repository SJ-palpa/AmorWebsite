CountDownTimer('11/8/2019 12:00 PM', 'countdown', 'progressBarCountdown'); //Month.Day

function CountDownTimer(dt, id, idprogressbar) {
    let end = new Date(dt);

    let _second = 1000;
    let _minute = _second * 60;
    let _hour = _minute * 60;
    let _day = _hour * 24;
    let timer;


    let now = new Date();
    let distance = end - now;
    let days = Math.floor(distance / _day);
    let pourcentage = 100 - (days/365)*100 ;
    document.getElementById(idprogressbar).style.width = pourcentage+'%' ;

    document.getElementById(idprogressbar).className = "progress-bar progress-bar-animated progress-bar-striped ";

    if (days < 250 && days >= 200) {
        document.getElementById(idprogressbar).className += 'bg-success';
    }
    else if (days < 200 && days >= 125) {
        document.getElementById(idprogressbar).className += 'bg-info';
    }
    else if (days < 125 && days >= 0) {
        document.getElementById(idprogressbar).className += 'bg-warning';
    }
    else if (days < 0){
        document.getElementById(idprogressbar).className += 'bg-danger';
    }

    function showRemaining() {
        let now = new Date();
        let distance = end - now;
        if (distance < 0) {

            clearInterval(timer);
            document.getElementById(id).innerHTML = 'Temps expiré';

            return;
        }
        let days = Math.floor(distance / _day);
        let hours = Math.floor((distance % _day) / _hour);
        let minutes = Math.floor((distance % _hour) / _minute);
        let seconds = Math.floor((distance % _minute) / _second);

        document.getElementById(id).innerHTML = 'Temps restant : ';
        document.getElementById(id).innerHTML += days + 'Days ';
        document.getElementById(id).innerHTML += hours + ':';
        document.getElementById(id).innerHTML += minutes + ':';
        document.getElementById(id).innerHTML += seconds ;


    }


    timer = setInterval(showRemaining, 1000);
}
