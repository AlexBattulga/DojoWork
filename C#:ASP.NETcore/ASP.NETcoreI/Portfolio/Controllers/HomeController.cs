using System;
using Microsoft.AspNetCore.Mvc;

namespace Portfolio.Controllers
{
    public class HomeController: Controller
    {
        // home page
        [HttpGet("")]
        public ViewResult Home()
        {
            return View();
        }
        // projects page
        [HttpGet("project")]
        public IActionResult Project()
        {
            return View();
        }
        // contact page
        [HttpGet("contact")]
        public IActionResult Contact()
        {
            return View();
        }
    }
}