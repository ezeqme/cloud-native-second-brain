---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Platform Engineering"
themes: ["Platform Engineering"]
speakers: ["Joe Kutner", "Salesforce"]
sched_url: https://kccncna2024.sched.com/event/1i7rD/this-platform-goes-to-11-boost-developer-productivity-with-lessons-from-salesforce-joe-kutner-salesforce
youtube_search_url: https://www.youtube.com/results?search_query=This+Platform+Goes+to+11%3A+Boost+Developer+Productivity+with+Lessons+from+Salesforce+CNCF+KubeCon+2024
slides: []
status: parsed
---

# This Platform Goes to 11: Boost Developer Productivity with Lessons from Salesforce - Joe Kutner, Salesforce

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: United States / Salt Lake City
- Speakers: Joe Kutner, Salesforce
- Schedule: https://kccncna2024.sched.com/event/1i7rD/this-platform-goes-to-11-boost-developer-productivity-with-lessons-from-salesforce-joe-kutner-salesforce
- Busca YouTube: https://www.youtube.com/results?search_query=This+Platform+Goes+to+11%3A+Boost+Developer+Productivity+with+Lessons+from+Salesforce+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre This Platform Goes to 11: Boost Developer Productivity with Lessons from Salesforce.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7rD/this-platform-goes-to-11-boost-developer-productivity-with-lessons-from-salesforce-joe-kutner-salesforce
- YouTube search: https://www.youtube.com/results?search_query=This+Platform+Goes+to+11%3A+Boost+Developer+Productivity+with+Lessons+from+Salesforce+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=97VCvHyHxGU
- YouTube title: This Platform Goes to 11: Boost Developer Productivity with Lessons from Salesforce - Joe Kutner
- Match score: 1.017
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/this-platform-goes-to-11-boost-developer-productivity-with-lessons-fro/97VCvHyHxGU.txt
- Transcript chars: 39552
- Keywords: platform, developers, developer, heroku, actually, experience, platforms, measure, hyperforce, productivity, interface, product, interfaces, salesforce, working, internal, important, across

### Resumo baseado na transcript

all right I guess we'll get started um thank you all for staying to the final hours of the conference just to see me I'm tickled uh I promise we're going to have fun here uh well I promise this will not be the most unfun talk you see this week uh I I like to use memes if you may have guessed and I'm going to use these memes to tell you a story a story about how we at Salesforce built uh a developer platform and as a

### Excerpt da transcript

all right I guess we'll get started um thank you all for staying to the final hours of the conference just to see me I'm tickled uh I promise we're going to have fun here uh well I promise this will not be the most unfun talk you see this week uh I I like to use memes if you may have guessed and I'm going to use these memes to tell you a story a story about how we at Salesforce built uh a developer platform and as a result our developers hated us because it was so bad but we spent the last two years fixing it making it better and we improved onboarding time inter Loop cycle time we gave developers tools that that you know let them do things they couldn't do before and today those same developers still hate us but at least they're more productive so so yeah um real quick I'm Joe cutner principal architect at Salesforce uh working on our internal platform uh with a focus on developer experience I spent uh before I was working on the internal stuff I spent about eight years at Heroku uh as a developer experienced architect and really cut my teeth there learning what it makes what it takes to build uh tools and experiences that developers really love that that Delight them uh while I was there uh I co-founded uh the cloud build packs project excuse me uh which is a a cncf incubating project we had a kiosk it's gone but I'll talk a little bit about how we use it today uh in in hyperforce so when I refer to our internal developer platform what I'm really talking about is what we call externally hyperforce now for our Salesforce customers uh hyperforce is not a developer platform this is something that underpins all the products that we sell at Salesforce and gives those non-developers or sometimes low code developers the same benefits of the cloud that we get from developer platforms uh security compliance Regional availability all those kinds of things internally when we're building those products we have our hyperforce developer platform so that that's what I'm going to be referring to not the external product uh Salesforce likes to name things after itself so whatever force hyperforce dreamforce is our big conference in San Francisco that shuts down the city for a week every year we just launched agent force an AI platform but today we're going to talk about a fictional product called meme Force meme Force combines the latest in AI technology with the best memes in the industry so we can give these to our customers right really important stuff this I want to
