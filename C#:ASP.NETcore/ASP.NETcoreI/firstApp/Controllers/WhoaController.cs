using Microsoft.AspNetCore.Mvc;
using System;

namespace firstApp.Controllers
{
    // Responds to user input
    // Routing...
    public class WhoaController: Controller
    {
        //localhost:5000/
        [HttpGet("")]
        public ViewResult Hello()
        {
            ViewBag.TimeFromWhoaController = DateTime.Now;
            return View();
        }
        //Redirect
        [HttpGet("hello")]
        public RedirectToActionResult RedirectStuff()
        {
            Console.WriteLine("We did it!!");
            return RedirectToAction("Hello");
        }
        //JSON
        [HttpGet("json")]
        public JsonResult JsonMe()
        {
            object myData = new
            {
                Name = " Devon",
                Words = new string []
                {
                    "Apple", "Shoe", "pizza"
                }
            };
            return Json(myData);
        }
    }
}