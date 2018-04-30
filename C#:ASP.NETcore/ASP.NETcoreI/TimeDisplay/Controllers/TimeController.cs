using System;
using Microsoft.AspNetCore.Mvc;

namespace TimeDisplay.Controllers
{
    public class TimeController: Controller
    {
        [HttpGet("")]
        public ViewResult Index()
        {
            DateTime time = DateTime.Now;
            string format = "MMM d, yyyy HH:MMtt";
            ViewBag.TimeFromTimeController = time.ToString(format);
            return View();
        }
    }
}