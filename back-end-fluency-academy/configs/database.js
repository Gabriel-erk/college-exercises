const  mongoose = require("mongoose");

mongoose.Promise = global.Promise;

const db = {};

db.mongoose = mongoose;
db.url = "mongodb://user:password@27017:27017/carrofacil?authSource=admin"

module.exports = db;