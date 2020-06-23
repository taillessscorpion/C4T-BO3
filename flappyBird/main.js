var everyNormalSecond, everyEndingSecond, everyBeginingSecond, playOrNot;
var flightAni;
var birdHeight, birdIndexX = 15;
var birdItself = document.getElementById("birdContainer");
var birdImg = document.getElementById("bird");
var playBtn = document.getElementById("playBtn");
var greetContainer = document.getElementById("greetContainer");
var greetContent = document.getElementById("greet");
var tubeContainer = document.getElementById("tubeContainer");
var tubePair = document.getElementsByClassName("tubePair");
var tube = document.getElementsByClassName("tube");
var tubePairPostition = [];
var points, highPoints = 0;
var score = document.getElementById("score");
var best = document.getElementById("best");
var sky = document.getElementsByClassName("sky");
var moutain = document.getElementsByClassName("moutain");
var ground = document.getElementsByClassName("ground");
var changeSrcOnTime;
var timingSky, timingGround, timingMoutain;
var tSky, tGround, tMoutain;
var skyIndex1, skyIndex2, skyIndex3;
var groundIndex1, groundIndex2, groundIndex3;
var moutainIndex1, moutainIndex2, moutainIndex3;
//100 > -100
//0 > -200
//-100 > -300

function MovingBackground(background1, background2, background3, moveIndex1, moveIndex2, moveIndex3) {
    background1.style.transform = "translateX("+moveIndex1+"%)";
    background2.style.transform = "translateX("+moveIndex2+"%)";
    background3.style.transform = "translateX("+moveIndex3+"%)";
}
function skyMove() {
    skyIndex1 -= 0.1;
    skyIndex2 -= 0.1;
    skyIndex3 -= 0.1;
    MovingBackground(sky[0], sky[1], sky[2], skyIndex1, skyIndex2);
    if(skyIndex1 == -100) {skyIndex1 = 100;};
    if(skyIndex2 == -200) {skyIndex2 = 0;};
    if(skyIndex3 == -300) {skyIndex3 = -100;};
    timingSky = setTimeout(skyMove, tSky);
}
function groundMove() {
    groundIndex1 -= 0.1;
    groundIndex2 -= 0.1;
    groundIndex3 -= 0.1;
    MovingBackground(ground[0], ground[1], ground[2], groundIndex1, groundIndex2);
    if(groundIndex1 == -100) {groundIndex1 = 100;};
    if(groundIndex2 == -200) {groundIndex2 = 0;};
    if(groundIndex3 == -300) {groundIndex3 = -100;};
    timingGround= setTimeout(groundMove, tGround);
}
function moutainMove() {
    moutainIndex1 -= 0.1;
    moutainIndex2 -= 0.1;
    moutainIndex3 -= 0.1;
    MovingBackground(moutain[0], moutain[1], moutain[2], moutainIndex1, moutainIndex2);
    if(moutainIndex1 == -100) {moutainIndex1 = 100;};
    if(moutainIndex2 == -200) {moutainIndex2 = 0;};
    if(moutainIndex3 == -300) {moutainIndex3 = -100;};
    timingMoutain = setTimeout(moutainMove, tMoutain);
}

function setTimeIndex() {
    skyIndex1 = 0;
    groundIndex1 = 0;
    moutainIndex1 = 0;
    skyIndex2 = 0;
    groundIndex2 = 0;
    moutainIndex2 = 0;
    skyIndex3 = -300;
    groundIndex3 = -300;
    moutainIndex3 = -300;
    tSky = 50;
    tGround = 20;
    tMoutain = 35;
}
function MoveOn() {
    clearTimeout(timingSky);
    clearTimeout(timingGround);
    clearTimeout(timingMoutain);
    skyMove();
    groundMove();
    moutainMove(); 
}
function MoveOff() {
    clearTimeout(timingSky);
    clearTimeout(timingGround);
    clearTimeout(timingMoutain);
}




function changeSrc(whichpic, whichsrc) {
    whichpic.setAttribute("src", whichsrc);
}
function changeSrcAtTP(whichpic, whichsrc, time) {
    setTimeout(function() {whichpic.setAttribute("src", whichsrc)}, time);
}

function changeHeightShow() {
    var showBirdHeight = "translate(15vw,"+ birdHeight +"vh)";
    birdItself.style.transform = showBirdHeight;
}
function gravity() {
    birdHeight += 0.3;
    if(birdHeight >= 80) {
        birdHeight = 75;
        birdImg.setAttribute("src", "photos/birdBrake.png");
        everyEndingSecond = setInterval(birdMoveOut, 33);
        gameOver();
    }
    changeHeightShow();
}
function ruledPlayZone(deepZone) {
    var topIndex = deepZone - 70;
    var botIndex = deepZone + 30;
    var showTopIndex = "translateY("+topIndex+"vh)";
    var showBotIndex = "translateY("+botIndex+"vh)";
    newTube = tubeContainer.children[tubeContainer.children.length-1].getElementsByClassName("tube");
    newTube[0].style.transform = showTopIndex;
    newTube[1].style.transform = showBotIndex;
}
function createNewTubePair() {
    var tubePairSample = document.createElement("div");
    var tubeSample1 = document.createElement("img");
    var tubeSample2 = document.createElement("img");
    tubeSample1.classList = "tube";
    tubeSample2.classList = "tube";
    tubePairSample.classList = "tubePair";
    tubeSample1.setAttribute("src", "photos/reverseTube.png");
    tubePairSample.appendChild(tubeSample1);
    tubeSample2.setAttribute("src", "photos/tube.png");
    tubePairSample.appendChild(tubeSample2);
    tubeContainer.appendChild(tubePairSample);
    var deepZone = Math.floor(Math.random() * 41) + 10;
    var tubeGivenInfo = {
        farIndex: 100,
        deadZone: deepZone,
    };
    ruledPlayZone(deepZone);
    tubePairPostition.push(tubeGivenInfo);
}
function tubeTouched() {
    if(birdHeight <= tubePairPostition[0].deadZone - 5 || birdHeight >= tubePairPostition[0].deadZone + 23.5) {
        clearTimeout(changeSrcOnTime);
        changeSrc(birdImg, "photos/birdAcc0.png");
        downIndex = 0;
        everyEndingSecond = setInterval(birdDropDown, 15);
        gameOver();
    }
}
function deletePassedTubePair() {
    tubeContainer.removeChild(tubeContainer.children[0]);
    tubePairPostition.shift();
}
function deleteAllTubePair() {
    for(d=0; d<tubePairPostition.length; d++) {
        tubeContainer.removeChild(tubeContainer.children[0]);
    }
    tubePairPostition = [];
}
function showTubePair(whichTube, where) {
    var showTubePair = "translate("+ where +"vw, 0)";
    tubePair[whichTube].style.transform = showTubePair;
}
function moveTubePair() {
    for(l=0; l<tubeContainer.children.length; l++) {
        tubePairPostition[l].farIndex = (tubePairPostition[l].farIndex - 0.25).toFixed(1);
        showTubePair(l, tubePairPostition[l].farIndex);
    }
}
function clearNumber(which) {
    var whichLength = which.children.length;
    for(d=0; d<whichLength; d++) {
        which.removeChild(which.children[0]);
    }
}
function showNumber(number, where) {
    var numberImg = document.createElement("img");
    numberImg.className = "number";
    numberImg.setAttribute("src", "photos/" + number + ".png");
    where.appendChild(numberImg);
}
function showPoint() {
    pointString = String(points);
    clearNumber(score, 0);
    for(s=pointString.length-1; s>-1; s--) {
    showNumber(pointString.charAt(s), score);
    };
}
function showHighPoint() {
    if(points > highPoints) {highPoints = points};
    pointString = String(highPoints);
    clearNumber(best, 1);
    for(s=pointString.length-1; s>-1; s--) {
    showNumber(pointString.charAt(s), best);
    };

}
function physicsRule() {
    if(tubeContainer.children.length == 0) {createNewTubePair();}
    else {
        if(tubePairPostition[tubePairPostition.length-1].farIndex == 70) {
            createNewTubePair();
        }
        else if(tubePairPostition[0].farIndex <= 20 && tubePairPostition[0].farIndex > 6) {
            tubeTouched();
        }
        else if(tubePairPostition[0].farIndex == 6) {
            points++;
            showPoint();
            showHighPoint();
        }
        else if(tubePairPostition[0].farIndex<= -10) {
            deletePassedTubePair();
        }
    }
    moveTubePair();
    gravity();
}



function changeHeight(time) {
    flightAni = setTimeout(function() {
        if(birdHeight <= 0) {
            birdHeight = 0;
        }
        else if(birdHeight > 0) {
            birdHeight--;
        }
    }, time);
}
function takeOff(e) {
    if(e.target != playBtn) {
        newHeight = Math.floor(Math.random() * 6);
        timeIndex = 10;
        for(t=0; t<25*timeIndex; t+=timeIndex) {
            changeHeight(t);
        }
        for(h=0; h<timeIndex*(newHeight+1); h+=timeIndex) {
            changeHeight(h);
        }

        changeSrc(birdImg, "photos/bird0.png");
        changeSrcOnTime = setTimeout(function() {birdImg.setAttribute("src", "photos/bird4.png")}, 125);
        changeSrcOnTime = setTimeout(function() {birdImg.setAttribute("src", "photos/bird3.png")}, 175);
        changeSrcOnTime = setTimeout(function() {birdImg.setAttribute("src", "photos/bird2.png")}, 300);
        changeSrcOnTime = setTimeout(function() {birdImg.setAttribute("src", "photos/bird1.png")}, 450);
        changeHeightShow();
    }
}
function birdMoveIn() {
    if(birdIndexX < 15) {
        birdHeight -= 1;
        birdIndexX++;
        birdPosition = "translate("+birdIndexX+"vw, "+birdHeight+"vh)";
        birdItself.style.transform = birdPosition;
    }
    
    else if(birdIndexX >= 15) {
        birdHeight = 30;
        birdIndexX = 15;
        birdItself.style.transform = "translate("+birdIndexX+", "+birdHeight+"vh)";
        clearInterval(everyBeginingSecond);
        everyNormalSecond = setInterval(physicsRule, 10);
        document.addEventListener("click", takeOff);
        document.addEventListener("keydown", takeOff);
        playBtn.addEventListener("mouseenter", btnPlayIn);
        playBtn.addEventListener("mousedown", btnPlayPress);
    };
}
function birdDropDown() {
    if(downIndex < 10) {downIndex++;}
    else if(downIndex == 10) {birdImg.setAttribute("src", "photos/birdAcc1.png"); downIndex++;}
    else if(downIndex > 10) {
        if(birdHeight <= 75) {
            birdHeight++;
            birdPosition = "translate("+birdIndexX+"vw, "+birdHeight+"vh)";
            birdItself.style.transform = birdPosition;
            if(Math.round(birdHeight) == 60) {
                birdImg.setAttribute("src", "photos/birdAcc2.png");
            }
            else if(Math.round(birdHeight) == 75) {
                birdImg.setAttribute("src", "photos/birdAcc3.png");
            };
        }
        else {
            clearInterval(everyEndingSecond);
            everyEndingSecond = setInterval(birdMoveOut, 33);
        };
    };
    
}
function birdMoveOut() {
    if(birdIndexX > -6) {birdIndexX--;}
    else if(birdIndexX <= -6) {
        clearInterval(everyEndingSecond);
        birdItself.style.opacity = 0;
    };
    birdPosition = "translate("+birdIndexX+"vw, "+birdHeight+"vh)";
    birdItself.style.transform = birdPosition;
}
function btnPlay() {
    playBtn.removeEventListener("mouseleave", btnPlay);
    changeSrc(playBtn, "photos/play.png", );
    playBtn.addEventListener("mouseenter", btnPlayIn);
}
function btnPlayIn() {
    playBtn.removeEventListener("mouseenter", btnPlayIn);
    changeSrc(playBtn, "photos/playHover.png");
    playBtn.addEventListener("mouseleave", btnPlay);
    playBtn.addEventListener("mousedown", btnPlayPress);
}
function btnPlayPress() {
    playBtn.removeEventListener("mouseleave", btnPlay);
    playBtn.removeEventListener("mousedown", btnPlayPress);
    changeSrc(playBtn, "photos/playChange1.png");
    changeSrcAtTP(playBtn, "photos/playChange2.png", 200);
    changeSrcAtTP(playBtn, "photos/pause.png", 400);
    playBtn.addEventListener("mouseenter", btnPauseIn);

    if(playOrNot == 0) {
        startGame();
        playBtn.removeEventListener("mouseleave", btnPauseIn);
    }
    else if(playOrNot == 2) {
        playGame();
    };
}
function btnPause() {
    playBtn.removeEventListener("mouseleave", btnPause);
    changeSrc(playBtn, "photos/pause.png");
    playBtn.addEventListener("mouseenter", btnPauseIn);
}
function btnPauseIn() {
    playBtn.removeEventListener("mouseenter", btnPauseIn);
    changeSrc(playBtn, "photos/pauseHover.png");
    playBtn.addEventListener("mouseleave", btnPause);
    playBtn.addEventListener("mousedown", btnPausePress);
}
function btnPausePress() {
    playBtn.removeEventListener("mouseleave", btnPause);
    playBtn.removeEventListener("mousedown", btnPausePress);
    changeSrc(playBtn, "photos/pauseChange1.png");
    changeSrcAtTP(playBtn, "photos/pauseChange2.png", 200);
    changeSrcAtTP(playBtn, "photos/play.png", 400);
    playBtn.addEventListener("mouseenter", btnPlayIn);
    pauseGame();
}

function startGame() {
    playOrNot = 1;
    greetContainer.style.opacity = 0;
    birdItself.style.opacity = 100;
    changeSrc(birdImg, "photos/bird1.png");
    birdIndexX = -5;
    birdHeight = 60;
    clearInterval(everyEndingSecond);
    clearInterval(everyNormalSecond);
    changeSrc(birdImg, "photos/bird0.png");
    var x = 130;
    setTimeout(function() {birdImg.setAttribute("src", "photos/bird4.png")}, 1*x);
    setTimeout(function() {birdImg.setAttribute("src", "photos/bird3.png")}, 2*x);
    setTimeout(function() {birdImg.setAttribute("src", "photos/bird2.png")}, 3*x);
    setTimeout(function() {birdImg.setAttribute("src", "photos/bird0.png")}, 4*x);
    setTimeout(function() {birdImg.setAttribute("src", "photos/bird4.png")}, 5*x);
    setTimeout(function() {birdImg.setAttribute("src", "photos/bird3.png")}, 6*x);
    setTimeout(function() {birdImg.setAttribute("src", "photos/bird1.png")}, 7*x);
    everyBeginingSecond = setInterval(birdMoveIn, 50);
    MoveOn();
}
function pauseGame() {
    playOrNot = 2;

    clearInterval(everyNormalSecond);
    document.removeEventListener("click", takeOff);
    document.removeEventListener("keydown", takeOff);
    MoveOff();
}
function playGame() {
    playOrNot = 1;

    clearInterval(everyEndingSecond);
    clearInterval(everyBeginingSecond);
    everyNormalSecond = setInterval(physicsRule, 10);
    document.addEventListener("click", takeOff);
    document.removeEventListener("keydown", takeOff);
    MoveOn();
}
function gameOver() {
    prepare();
    showPoint()
    clearInterval(everyNormalSecond);
    document.removeEventListener("click", takeOff);
    document.removeEventListener("keydown", takeOff);
    deleteAllTubePair();

    changeSrc(greetContent, "photos/gameOver.png");

    playBtn.removeEventListener("mouseleave", btnPause);
    playBtn.removeEventListener("mouseenter", btnPauseIn);
    playBtn.removeEventListener("mousedown", btnPausePress);
}

function prepare() {
    playOrNot = 0;
    points = 0;
    setTimeIndex();
    clearNumber(score, 0);
    showHighPoint();
    changeSrc(greetContent, "photos/startGame.png");
    changeSrc(playBtn, "photos/play.png");
    greetContainer.style.opacity = 100;
    playBtn.addEventListener("mouseenter", btnPlayIn);
    playBtn.addEventListener("mousedown", btnPlayPress);
}

prepare();
document.getElementById("fullScreen").draggable = false;