---
type: promcon-talk
conference: PromCon
edition: "PromCon 2016"
edition_id: 2016-berlin
year: 2016
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2016-berlin/talks/deploying-prometheus-at-digitalocean/
youtube_url: https://www.youtube.com/watch?v=ieo3lGBHcy8
youtube_search_url: https://www.youtube.com/results?search_query=Deploying+Prometheus+at+DigitalOcean+PromCon+2016
video_match_score: 0.857
status: video-found
---

# Deploying Prometheus at DigitalOcean

## Identificação

- Edição: PromCon 2016
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2016-berlin/talks/deploying-prometheus-at-digitalocean/
- YouTube: https://www.youtube.com/watch?v=ieo3lGBHcy8

## Resumo

Speaker: Carlos Amedee This talk focuses on how we use configuration management at DigitalOcean to deploy and maintain many instances of Prometheus. We will discuss the benefits and challenges of deploying Prometheus at a large scale.

## Abstract oficial

Speaker: Carlos Amedee

This talk focuses on how we use configuration management at DigitalOcean to
deploy and maintain many instances of Prometheus. We will discuss the benefits
and challenges of deploying Prometheus at a large scale.

## Links

- Página oficial: https://promcon.io/2016-berlin/talks/deploying-prometheus-at-digitalocean/
- YouTube: https://www.youtube.com/watch?v=ieo3lGBHcy8
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ieo3lGBHcy8
- YouTube title: PromCon 2016: Deploying Prometheus at DigitalOcean - Carlos Amedee
- Match score: 0.857
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2016/deploying-prometheus-at-digitalocean/ieo3lGBHcy8.txt
- Transcript chars: 31421
- Keywords: prometheus, exporter, exporters, metrics, company, create, deployed, simple, cookbooks, deploying, software, infrastructure, engineers, source, trying, little, learned, actually

### Resumo baseado na transcript

uh we have carlos amended here he is working at digitalocean currently still getting a master's degree at georgia tech and he really loves distributed systems and he's going to tell you about deploying prometheus at digitalocean another digital ocean talk but i think it's going to focus on something else yes can everybody hear me yeah um so yes i'm the third person to talk from digitalocean this weekend or this conference so instead of being a technical talk i'm going to lean towards being a social talk so

### Excerpt da transcript

uh we have carlos amended here he is working at digitalocean currently still getting a master's degree at georgia tech and he really loves distributed systems and he's going to tell you about deploying prometheus at digitalocean another digital ocean talk but i think it's going to focus on something else yes can everybody hear me yeah um so yes i'm the third person to talk from digitalocean this weekend or this conference so instead of being a technical talk i'm going to lean towards being a social talk so this is deploying prometheus at digital ocean the the care and feeding of prometheus digitalocean for the third time you'll hear this this weekend um or this this conference is a cloud services provider we focus on simplicity we have a virtual machine offering which we call droplets we also have block storage we have virtual ips um and many things coming in the future so if you haven't tried us give us a try we're a decent company well i'm a software engineer i was i was in the metrics team at digitalocean i am now in a team called the agent team some people call it the secret agent team um which means i probably won't talk about what i'm currently working on but as mentioned i'm a master's in computer science candidate at uh georgia tech um i am a lover of find metrics um and you see my twitter handle here so i'll give you some stats about prometheus at digit ocean from a very lightweight check earlier today or yesterday we have more than 80 instances of prometheus running in our infrastructure we have more than 15 types of exporters deployed internally we have more than five exporters that were written in-house that are not open source they're sort of custom exporters for our infrastructure and we have six of open source um exporters which were written you know uh by employees of the company and uh open sourced our internal the the relevant internal architecture or the relevant internal uh architectural components for this particular talk are um like our rails apps we have a couple of fairly large rails apps and um we have a lot of grow micro services which means a lot of complexity so the i want to i want to discuss so we're trying to touch on the social aspect of deploying software um or deploying an open source ecosystem and encouraging people within the company to use it one thing we did not do at digitalocean is force people to use it it's not a mandate to use prometheus someone started working with it and eventually it just became the the new hot
