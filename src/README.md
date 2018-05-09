# Frame2video

## MVP

take an S3 and make some videos

detour: use local FS for now.


## User stories

### All frames

upload a pile of images to an S3 bucket and make a video of _all_ of them

### Pick frames

Choose what farmes are used:
* By time perion : 1/h 1/day
* By light levels: only day time, Only night time
* By "interesting" : only frames with motion in them

## Pick output formats:

* an output format
* post to S3 bucket
* post to youtube
* Others?

## Requirements / Supporting Bits

* the S3 bucket where the frames are.
* the s3 bucket where the video goes
* the datastore ( TBD ) where the persistant stuff goes

## Backlog

* Testing
* Coverage measure
* user authentication
* contract auth
* "mutli cloud"
** AWS S3
** GCP Cloud Storage
** Azure Stoarge Account

* https://12factor.net/
** Config
** concurancy / locking
* Automated inf setup
* container it

# Administration

Dev startup
 FLASK_ENV=development CONFIG_FILE="dev.cfg" flask run --host=0.0.0.0

Prod startup:
 CONFIG_FILE="prod.cfg" flask run --host=0.0.0.0

