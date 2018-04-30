using System;
using System.Collections.Generic;
using Microsoft.AspNetCore.Mvc;

namespace DojoSurvey.Controllers
{
    public class SurveyController: Controller
    {
        // index page
        [HttpGet("")]
        public IActionResult Survey()
        {
            return View();
        }
        // getting a data from form.
        [HttpPost("formData")]
        public IActionResult UserData(string fullname, string location, string language, string text)
        {
            ViewBag.Name = fullname;
            ViewBag.Location = location;
            ViewBag.Language = language;
            ViewBag.Text = text;
            return View();
        }
    }
}