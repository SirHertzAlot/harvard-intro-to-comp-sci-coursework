document.addEventListener('DOMContentLoaded', function(){
  let month = months[dte.getMonth()];
  let next_month = document.getElementById("next_month");
  let last_month = document.getElementById("last_month");
  
  next_month.addEventListener('click', function(){
    let current_month;
    if(months.includes(month))
    {
      if(window.location.search.includes("month="))
      {
        month = window.location.search.split("=")[1].replace("month=","");
        current_month = months.indexOf(month);
      }
      if(current_month == 11){
        current_month = 0;
      } else {
        current_month = months.indexOf(month);
        current_month++;
      }
      return window.location.href = `https://f8d46676-d318-40da-87b6-899cff4d6f58-00-1vvj5xa7dhwru.worf.replit.dev/api/calendarView?month=${months[current_month]}`;
    }
  });

  last_month.addEventListener('click', function(){ 
    month = window.location.search.split("=")[1].replace("month=","");
    if(months.includes(month))
    {
      if(window.location.search.includes("month="))
      {
        let current_month = months.indexOf(month);
        if(current_month == 0){
          current_month = 11;
        } else {
          current_month--;
        }
        return window.location.href = `https://f8d46676-d318-40da-87b6-899cff4d6f58-00-1vvj5xa7dhwru.worf.replit.dev/api/calendarView?month=${months[current_month]}`;
      }
    }
  });
});