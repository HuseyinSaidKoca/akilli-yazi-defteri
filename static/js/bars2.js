const bars = document.querySelectorAll('.bar');
const progress = document.querySelectorAll('.progress');
const {MongoClient} = require('mongodb');
const uri = "mongodb://localhost:27017/okul";
const client = new MongoClient(uri);
const mongoose = require(‘mongoose’)
bars.forEach((bar, index) => {
  //veri al
  bar.style.width = `${randomWidth}%`;

})
