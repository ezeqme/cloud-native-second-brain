---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Security"
themes: ["AI ML", "Security", "Runtime Containers"]
speakers: ["Carmen Chow", "Thomas Robinson", "Yelp"]
sched_url: https://kccncna2024.sched.com/event/1i7o2/from-standards-to-practice-the-journey-to-container-maturity-carmen-chow-thomas-robinson-yelp
youtube_search_url: https://www.youtube.com/results?search_query=From+Standards+to+Practice%3A+The+Journey+to+Container+Maturity+CNCF+KubeCon+2024
slides: []
status: parsed
---

# From Standards to Practice: The Journey to Container Maturity - Carmen Chow & Thomas Robinson, Yelp

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]], [[Runtime Containers]]
- País/cidade: United States / Salt Lake City
- Speakers: Carmen Chow, Thomas Robinson, Yelp
- Schedule: https://kccncna2024.sched.com/event/1i7o2/from-standards-to-practice-the-journey-to-container-maturity-carmen-chow-thomas-robinson-yelp
- Busca YouTube: https://www.youtube.com/results?search_query=From+Standards+to+Practice%3A+The+Journey+to+Container+Maturity+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre From Standards to Practice: The Journey to Container Maturity.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7o2/from-standards-to-practice-the-journey-to-container-maturity-carmen-chow-thomas-robinson-yelp
- YouTube search: https://www.youtube.com/results?search_query=From+Standards+to+Practice%3A+The+Journey+to+Container+Maturity+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=QeR3jeLs_l0
- YouTube title: From Standards to Practice: The Journey to Container Maturity - Carmen Chow & Thomas Robinson, Yelp
- Match score: 0.864
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/from-standards-to-practice-the-journey-to-container-maturity/QeR3jeLs_l0.txt
- Transcript chars: 32891
- Keywords: container, containers, basically, security, within, characteristics, question, provide, management, standards, thinking, maturity, answer, talking, checks, component, environment, already

### Resumo baseado na transcript

so first of all thank you for joining us everybody um how's your coupon been so far excellent so quick show of hands how many of you have been at the uh platform engineering or observability talks this week it's a pretty good number how many of you gone to the security talks this week also a pretty good number I'm impressed so if you've been to any of those three types of talks you came to the right place so our talk today is about uh containers from standards

### Excerpt da transcript

so first of all thank you for joining us everybody um how's your coupon been so far excellent so quick show of hands how many of you have been at the uh platform engineering or observability talks this week it's a pretty good number how many of you gone to the security talks this week also a pretty good number I'm impressed so if you've been to any of those three types of talks you came to the right place so our talk today is about uh containers from standards to practice the journey to container maturity um quick intro to who we are off on the right I'm Tom Robinson I've been with theel for 12 years gosh it's been a long time um mostly work working on uh backend Services um and working on keeping ELP secure before that I did AV my free time I make video games Carmen hi I'm Carmen I've been at Yelp for about two years and started working on this project with Tom a year ago and yeah happy to be here happy to be here as well all right so our talk today is split into four sections um the problem the journey the model and the takeaways um there should be ample time to uh have qu Q&A at the end uh my time this is about 25 30 minutes um so just keep your questions for the end we'll and we'll be able to answer those we'll also be in the hall afterwards so problem so for most of the time this week you've probably been thinking been thinking about your application at scale we've been talking about kubernetes your instrumentation platform we've been talking about your Security Solutions sort of at the macro level um but here we're here to talk about containers why containers specifically because you might think of that as kind of a smaller component well the answer is if you're thinking about this from the perspective of an attacker they usually start inside of the container um so let's say they they pwn a box or pwn a little one of your containers running in a pod um first thing they're going to do is you know look at aty shadow look at the process space and be like okay we see this application running what does it mean and then they're going to start to breed the configuration they're going to try to sort of gain leverage and they they'll come be in there and saying saying oh wait there's data in here what happens if they see your container connected to three different S3 buckets and all those are just you know set to read and they have your crown jewels well that's bad um so that that person is basically going to get you know take their hoodie go like this I don'
