using System;
using System.Collections.Generic;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace Dojodachi.Controllers
{
    public class DojodachiController : Controller
    {
        // index page
        [HttpGet("")]
        public ViewResult Index()
        {;
            // ViewBag.Message = new List<string>();
            int? fullness = HttpContext.Session.GetInt32("fullness");
            int? happiness = HttpContext.Session.GetInt32("happiness");
            int? energy = HttpContext.Session.GetInt32("energy");
            int? meal = HttpContext.Session.GetInt32("meal");
            // checking a fillness's value
            if(fullness == null){
                fullness = 20;
                HttpContext.Session.SetInt32("fullness", 20);
            }
            // checking a happiness's value
            if(happiness == null){
                happiness = 20;
                HttpContext.Session.SetInt32("happiness", 20);
            }
            // checking a enery's value
            if(energy == null){
                energy = 50;
                HttpContext.Session.SetInt32("energy", 50);
            }
            // checking a meal's value
            if(meal == null){
                meal = 3;
                HttpContext.Session.SetInt32("meal", 3);
            }
            HttpContext.Session.SetInt32("fullness", (int)fullness);
            HttpContext.Session.SetInt32("happiness", (int)happiness);
            HttpContext.Session.SetInt32("energy", (int)energy);
            HttpContext.Session.SetInt32("meal", (int)meal);
            ViewBag.Message = TempData["message"];
            ViewBag.Fullness = fullness;
            ViewBag.Happiness = happiness;
            ViewBag.Energy = energy;
            ViewBag.Meal = meal;
            if(ViewBag.Fullness >= 100 && ViewBag.Happiness >= 100 && ViewBag.Energy >= 100){
                ViewBag.msg ="Congratulations! You won!";
            }
            if(ViewBag.Fullness <= 0 || ViewBag.Happiness <= 0){
                ViewBag.msg ="Your Dojodachi has passed away...";
            }
            if(ViewBag.Meal == 0){
                ViewBag.msg = ("No meal to feed");
            }
            return View();
        }
        [HttpGet("feed")]
        public IActionResult Feed()
        {
            Random rand = new Random();
            int? meal = HttpContext.Session.GetInt32("meal");
            int? fullness = HttpContext.Session.GetInt32("fullness");
            int bonus = rand.Next(5, 11);
            
            if(meal > 0)
            {
                meal -= 1;
                fullness += bonus;
            }
            
            HttpContext.Session.SetInt32("fullness", (int)fullness);
            HttpContext.Session.SetInt32("meal", (int)meal);
            TempData["message"] = ($"You played with your Dojodachi Fullness +{bonus}, Meal -1");
            return RedirectToAction("Index");
        }
        [HttpGet("Play")]
        public IActionResult Play()
        {
            Random rand = new Random();
            int? energy = HttpContext.Session.GetInt32("energy");
            int? happiness = HttpContext.Session.GetInt32("happiness");
            int bonus = rand.Next(5, 11);
            if(energy > 0){
                energy -= 5;
                happiness += bonus;
            }
            HttpContext.Session.SetInt32("energy", (int)energy);
            HttpContext.Session.SetInt32("happiness", (int)happiness);
            TempData["message"] =($"You played with your Dojodachi Happiness +{bonus}, Energy -5");
            return RedirectToAction("Index");
        }
        [HttpGet("work")]
        public IActionResult Work()
        {
            Random rand = new Random();
            int? energy = HttpContext.Session.GetInt32("energy");
            int? meal = HttpContext.Session.GetInt32("meal");
            int bonus = rand.Next(1, 4);
            if(energy > 0){
                 energy -= 5;
                 meal += bonus;
            }
            HttpContext.Session.SetInt32("energy", (int)energy);
            HttpContext.Session.SetInt32("meal", (int)meal);
            TempData["message"] =($"You played with your Dojodachi Meal +{bonus}, Energy -5");
            return RedirectToAction("Index");
        }
        [HttpGet("sleep")]
        public IActionResult Sleep()
        {
            int? energy = HttpContext.Session.GetInt32("energy");
            int? happiness = HttpContext.Session.GetInt32("happiness");
            int? fullness = HttpContext.Session.GetInt32("fullness");
            if(happiness > 0 || fullness > 0 || energy >0){
                energy += 15;
                fullness -= 5;
                happiness -= 5;
            }
            HttpContext.Session.SetInt32("energy", (int)energy);
            HttpContext.Session.SetInt32("happiness", (int)happiness);
            HttpContext.Session.SetInt32("fullness", (int)fullness);
            TempData["message"] = ($"You played with your Dojodachi Enegry +15, Fullness and Happiness -5");
            return RedirectToAction("Index");
        }
        [HttpGet("clear")]
        public IActionResult Clear()
        {
            HttpContext.Session.Clear();
            return RedirectToAction("Index");
        }
    }
}