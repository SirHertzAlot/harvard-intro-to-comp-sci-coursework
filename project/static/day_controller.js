document.addEventListener('DOMContentLoaded', function(){
    let current_month = months[dte.getMonth()];
    let next_month = months[months.indexOf(current_month) + 1];
    let yesterday = document.getElementById("yesterday");
    let tomorrow = document.getElementById("tomorrow");
    let lastDayOfMonth = new Date(dte.getFullYear(), dte.getMonth()+1, 0);

    yesterday.addEventListener('click', function(){
      let today = dte.getDate();
      current_month = months[dte.getMonth()]
      if(window.location.search.includes("today="))
      {
        today = window.location.search.split("=")[1].replace("&month", "");
        today--;
        if(window.location.search.includes("month=")){
          today = window.location.search.split("=")[1].replace("&month", "");
          today--;
          month = window.location.search.split("=")[2].replace("&a","");
          monthIndex = months.indexOf(month);
          if(today < 1)
          {
            let last_date = lastDayOfMonth.getDate();
            let prevMonth = months[monthIndex - 1];
            lastDayOfMonth = new Date(dte.getFullYear(), monthIndex + 1, 0);
            console.log(lastDayOfMonth);
            return window.location.href = `https://f8d46676-d318-40da-87b6-899cff4d6f58-00-1vvj5xa7dhwru.worf.replit.dev/daysView?today=${last_date}&month=${encodeURIComponent(prevMonth)}&a=yesterday`
          }
          return window.location.href = `https://f8d46676-d318-40da-87b6-899cff4d6f58-00-1vvj5xa7dhwru.worf.replit.dev/daysView?today=${encodeURIComponent(today)}&month=${encodeURIComponent(month)}&a=yesterday`
        }
        return window.location.href = `https://f8d46676-d318-40da-87b6-899cff4d6f58-00-1vvj5xa7dhwru.worf.replit.dev/daysView?today=${encodeURIComponent(today)}&month=${encodeURIComponent(current_month)}`;
      }
      return window.location.href = `https://f8d46676-d318-40da-87b6-899cff4d6f58-00-1vvj5xa7dhwru.worf.replit.dev/daysView?today=${encodeURIComponent(today)}&month=${encodeURIComponent(current_month)}&a=yesterday`;
    });

    tomorrow.addEventListener('click', function(){
      let today = dte.getDate();
      current_month = months[dte.getMonth()]
      if(window.location.search.includes("today="))
      {
        today = window.location.search.split("=")[1].replace("&month", "");
        today++;
        if(window.location.search.includes("month=")){
          month = window.location.search.split("=")[2].replace("&a","");
          monthIndex = months.indexOf(month);
          lastDayOfMonth = new Date(dte.getFullYear(), monthIndex + 1, 0);
          if(today > lastDayOfMonth.getDate())
          {
            next_month = months[monthIndex + 1]
            today = 1;
            return window.location.href = `https://f8d46676-d318-40da-87b6-899cff4d6f58-00-1vvj5xa7dhwru.worf.replit.dev/daysView?today=${encodeURIComponent(today)}&month=${encodeURIComponent(next_month)}&a=tomorrow`;
          }
          return window.location.href = `https://f8d46676-d318-40da-87b6-899cff4d6f58-00-1vvj5xa7dhwru.worf.replit.dev/daysView?today=${encodeURIComponent(today)}&month=${encodeURIComponent(month)}&a=tomorrow`;
        }
        return window.location.href = `https://f8d46676-d318-40da-87b6-899cff4d6f58-00-1vvj5xa7dhwru.worf.replit.dev/daysView?today=${encodeURIComponent(today)}&month=${encodeURIComponent(current_month)}`;
      }
      return window.location.href = `https://f8d46676-d318-40da-87b6-899cff4d6f58-00-1vvj5xa7dhwru.worf.replit.dev/daysView?today=${encodeURIComponent(today)}&month=${encodeURIComponent(current_month)}&a=tomorrow`;
    });
});

