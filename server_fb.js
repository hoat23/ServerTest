'use strict';
//Import dependencias and set up http server
const 
    express = require('express'),
    bodyParser = require('body-parser'),
    app = express().use(bodyParser.json()); //Create express http server

//Set server port an logs message on success
app.listen(process.env.PORT || 4006, ()=> console.log('[INFO] webhook facebook listening'));


app.post('/webhook', (req, res)=>{
    let datetime = new Date();
    let body = req.body;
    //Checks this is an event from a page subscription
    if (body.object == 'page') {
        //Iterates over each entry - there may be multiple if batched
        body.entry.array.forEach( function(entry){
            //Getting the message. entry.messaging is an array, but
            //will only contain one message, so we get index 0
            let webhook_event = entry.messaging[0];
            console.info("webhook_event = [%s]", webhook_event);
        });
        res.status(200).send('EVENT_RECEIVED');
    }else{
        console.warn("%s|ERROR| webhook_event|404| Event isn't from page subscription | %s |",datetime.toISOString(), body.object);
        res.sendStatus(404);
    }
});

// Adds support for GET requests to our webhook
app.get('/webhook', (req, res) => {
    // Your verify token. Should be a random string.
    let VERIFY_TOKEN = "b7fac9153679d54790e630d804516238553b7a13"
    let datetime = new Date();
    // Parse the query params
    let mode = req.query['hub.mode'];
    let token = req.query['hub.verify_token'];
    let challenge = req.query['hub.challenge'];
      
    // Checks if a token and mode is in the query string of the request
    if (mode && token) {
    
      // Checks the mode and token sent is correct
      if (mode === 'subscribe' && token === VERIFY_TOKEN) {
        
        // Responds with the challenge token from the request
        console.log('%s|INFO| WEBHOOK_VERIFIED | mode=subscribe',datetime.toISOString());
        res.status(200).send(challenge);
      
      } else {
        // Responds with '403 Forbidden' if verify tokens do not match
        res.sendStatus(403);      
      }
    }
  });

//https://developers.facebook.com/docs/messenger-platform/getting-started/webhook-setup/?locale=es_ES

//Verificar server_fb
//curl -X GET "localhost:4006/webhook?hub.verify_token=b7fac9153679d54790e630d804516238553b7a13&hub.challenge=CHALLENGE_ACCEPTED&hub.mode=subscribe"

//Testing sending data
//curl -H "Content-Type: application/json" -X POST "localhost:1337/webhook" -d '{"object": "page", "entry": [{"messaging": [{"message": "TEST_MESSAGE"}]}]}'
