---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Project Opportunities"
themes: ["AI ML", "Community Governance"]
speakers: ["Eduardo Silva", "Maintainer"]
sched_url: https://kccncna2025.sched.com/event/27d5X/project-lightning-talk-fluent-bit-eduardo-silva-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Fluent+Bit+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Fluent Bit - Eduardo Silva, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Eduardo Silva, Maintainer
- Schedule: https://kccncna2025.sched.com/event/27d5X/project-lightning-talk-fluent-bit-eduardo-silva-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Fluent+Bit+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Fluent Bit.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27d5X/project-lightning-talk-fluent-bit-eduardo-silva-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Fluent+Bit+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6m0vgUeYkNc
- YouTube title: Project Lightning Talk: Fluent Bit - Eduardo Silva, Maintainer
- Match score: 0.805
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-fluent-bit/6m0vgUeYkNc.txt
- Transcript chars: 5080
- Keywords: fluent, performance, analysis, multiple, achieve, solution, routing, destination, cubecon, lightning, around, thanks, pretty, cost, volume, actually, collect, scenario

### Resumo baseado na transcript

Well, thanks for coming and this will be uh as all the lightning talks very short and I would like to know pretty quickly who's as fluent bit user maybe if okay so half of you know this tool and half of you want to know more. One of the problems in in this space is that we generate ton and ton of data right and the only prediction that we have is like many times cost goes up right the volume of data is going up like crazy okay so this Sometimes they use a Splunk not because they love it but because hey they're laughing right because you need some realtime search and texting is pretty good but that has a cost. So one problem to solve all this stuff from moving data at scale is done with fluent bit for those who are new to the solution and fluent bit is everywhere and fluent bit project has been driven by a few principles since the beginning like high performance but low resource usage being a vendor neutral solution that also is easy to integrate as a project we don't want that you go and replace what you have actually we want to give you something that you just do some kind We have enhanced also the security mechanism when loading certificates when using OpenSSL in certain environments.

### Excerpt da transcript

Good afternoon. How are you? I have to wake you up guys. I know that's really cold outside and we need to move around. Well, thanks for coming and this will be uh as all the lightning talks very short and I would like to know pretty quickly who's as fluent bit user maybe if okay so half of you know this tool and half of you want to know more. One of the problems in in this space is that we generate ton and ton of data right and the only prediction that we have is like many times cost goes up right the volume of data is going up like crazy okay so this is a fact and year over year this will grow no matter what however you don't care about too much the data actually if you think why we collect the data is because you want to gather some analysis is some results from analysis from that data that give you some insights to take some decisions and the reality is like you have to deal with this scenario right logs matrix traces multiple applications Java cobalt whatever right and how do you achieve this data analysis if you are in this scenario and if you think about microservices where this application are distributed or maybe you have a thousand replicas of one app right it gets a little messy and guess But our users, you always want more performance, more performance, right?

But if the volume of data is going up like crazy, how do we achieve that? Yeah, there are different ways to scale, right? But the most interesting way will be like how we can have a solution that scales over time and always optimizing for performance. And at the end of the day, if you consume less CPU, less memory, you pay less, right? That's what matters. And to achieve this also you have a huge environment with multiple sources of data and likely multiple destinations. Usually companies don't send the data to one just one back end. They use S3 because it's cheap. Sometimes they use a Splunk not because they love it but because hey they're laughing right because you need some realtime search and texting is pretty good but that has a cost. So one problem to solve all this stuff from moving data at scale is done with fluent bit for those who are new to the solution and fluent bit is everywhere and fluent bit project has been driven by a few principles since the beginning like high performance but low resource usage being a vendor neutral solution that also is easy to integrate as a project we don't want that you go and replace what you have actually we want to give you something that you j
