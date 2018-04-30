using System;
using System.Collections.Generic;
using Microsoft.AspNetCore.Mvc;
using Newtonsoft.Json;

namespace PokeApi.Controllers
{
    public class PokeController : Controller
    {
        [HttpGet("{id}")]
        public IActionResult Poke(int id = 3)
        {
            WebRequest.GetPokeApiAsync(id, Callback =>
            {
                ViewBag.Poke = Callback;
            }).Wait();
            if(ViewBag.Poke == null)
            {
                ViewBag.Poke = new Dictionary<string, object>();
            }
            return View();
        }
    }
}