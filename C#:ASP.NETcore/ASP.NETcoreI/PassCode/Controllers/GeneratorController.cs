using System;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using System.Collections.Generic;

namespace PassCode.Controllers
{
    public class GeneratorController : Controller
    {
        // index page
        [HttpGet("")]
        public ViewResult Index()
        {
            int? count = HttpContext.Session.GetInt32("count");
            if( count == null)
                count = 1;
                HttpContext.Session.SetInt32("count", 1);
            HttpContext.Session.SetInt32("count", (int)count);
            // generating 14 length of passcode
            string PossibleCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
            string PassCode = "";
            Random Rand = new Random();
            for(int i = 0; i < 14; i++)
            {
                PassCode = PassCode + PossibleCharacters[Rand.Next(0, PossibleCharacters.Length)];
            }
            ViewBag.PassCode = PassCode;
            ViewBag.Count = count;
            return View("CodeGenerator");
        }
        // Generate passcode
        [HttpGet("process")]
        public IActionResult Process()
        {
            // incrementing count by 1
            int? count = HttpContext.Session.GetInt32("count");
            count++;
            HttpContext.Session.SetInt32("count", (int)count);
            
            return RedirectToAction("Index");
        }
        //Clear session
        [HttpGet("clear")]
        public IActionResult Clear()
        {
            HttpContext.Session.Clear();
            return RedirectToAction("Index");
        }
    }
}