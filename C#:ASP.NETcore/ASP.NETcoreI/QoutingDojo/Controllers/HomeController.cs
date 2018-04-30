using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using QoutingDojo.Models;
using DbConnection;

namespace QoutingDojo.Controllers
{
    public class HomeController : Controller
    {
        [HttpGet("")]
        public IActionResult Index()
        {
            ViewBag.Errors = new List<string>();
            return View();
        }
        [HttpPost("process")]
        public IActionResult Process(string fullname, string text)
        {
            ViewBag.Errors = new List<string>();
            // check if fullname field is not null or more than 5 characters!!!
            if(fullname == null)
            {
                ViewBag.Errors.Add("Fullname field is required!");
            }
            else if (fullname.Length < 6)
            {
                ViewBag.Errors.Add("Fullname must be more than 5 letters!");
            }
            // check quote field is not null
            if(text == null)
            {
                ViewBag.Errors.Add("Quote field cannot be empty!");
            }
            if(ViewBag.Errors.Count > 0)
            {
                return View("Index");
            }else
            {
                string query = $"INSERT INTO users(fullname, qoute, created_at) VALUES ('{fullname}', '{text}', NOW())";
                DbConnector.Execute(query);
                return RedirectToAction("Success");
            }
        }
        [HttpGet("success")]
        public IActionResult Success()
        {
            List<Dictionary<string, object>> AllUsers = DbConnector.Query("SELECT * FROM users");
            ViewBag.myData = AllUsers.OrderByDescending(des => des["created_at"]).ToList();
            return View();
        }
    }
}
