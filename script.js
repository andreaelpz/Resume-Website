function openPopup() {
    var button = document.querySelector("button");
    var popupContainer = document.getElementById("popupContainer");
    var popupContent = document.getElementById("popupContent");
  
    var buttonPosition = button.getBoundingClientRect();
    var buttonCenterX = buttonPosition.left + button.offsetWidth / 2;
    var buttonCenterY = buttonPosition.top + button.offsetHeight / 2;
  
    var popupWidth = 400;
    var popupHeight = 200;
    var popupLeft = buttonCenterX - popupWidth / 2;
    var popupTop = buttonCenterY - popupHeight / 2;
  
    popupContainer.style.width = "100%";
    popupContainer.style.height = "100%";
  
    popupContent.style.width = popupWidth + "px";
    popupContent.style.height = popupHeight + "px";
    popupContent.style.left = popupLeft + "px";
    popupContent.style.top = popupTop + "px";
  }
  