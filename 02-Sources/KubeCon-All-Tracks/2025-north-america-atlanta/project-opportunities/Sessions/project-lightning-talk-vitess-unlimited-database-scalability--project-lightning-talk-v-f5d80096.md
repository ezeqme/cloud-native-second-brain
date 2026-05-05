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
themes: ["AI ML", "Storage Data", "SRE Reliability", "Community Governance"]
speakers: ["Matt Lord", "Maintainer"]
sched_url: https://kccncna2025.sched.com/event/27d5v/project-lightning-talk-vitess-unlimited-database-scalability-matt-lord-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Vitess%3A+Unlimited+Database+Scalability+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Vitess: Unlimited Database Scalability - Matt Lord, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Storage Data]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Matt Lord, Maintainer
- Schedule: https://kccncna2025.sched.com/event/27d5v/project-lightning-talk-vitess-unlimited-database-scalability-matt-lord-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Vitess%3A+Unlimited+Database+Scalability+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Vitess: Unlimited Database Scalability.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27d5v/project-lightning-talk-vitess-unlimited-database-scalability-matt-lord-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Vitess%3A+Unlimited+Database+Scalability+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=CSSnY3MFhPI
- YouTube title: Project Lightning Talk: Vitess: Unlimited Database Scalability - Matt Lord, Maintainer
- Match score: 0.931
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-vitess-unlimited-database-scalability/CSSnY3MFhPI.txt
- Transcript chars: 6187
- Keywords: vitess, interfacing, production, traffic, database, called, actually, course, manage, across, replicas, unlimited, primary, encounter, maintainer, scalable, highly, available

### Resumo baseado na transcript

So, my primary goal with this talk is just to help raise awareness of Vitess. So that in the future, you know, when you encounter a use case that might be ideal for Vitess, uh, Vitess will pop up in the back of your mind. On top of just being MySQL compatible and allowing you to scale, it has a lot of very nice features on top of that. Uh backup and recovery of course is an important thing and it makes it gives you a lot of easy options for that and a lot of other things that we're going to talk a bit more that just allow you to to scale. So this is just a sample of companies at a very large scale that are using Vitess in production today and that I hope give you uh some confidence to to try it out yourself when you encounter uh hopefully an ideal use case. So some of the principles and features that allow us to help you scale is isolation.

### Excerpt da transcript

All right. Um, who here has ever heard of the CNCF project called Vitess? Oh, it's actually more than I expected. Um, that's nice to see. U, but still a small fraction of the people that are here. So, my primary goal with this talk is just to help raise awareness of Vitess. We'll talk about what it is and why it might be interesting. So that in the future, you know, when you encounter a use case that might be ideal for Vitess, uh, Vitess will pop up in the back of your mind. You'll say, "Hey, I remember this thing this weird looking guy at CubeCon a while back was talking about. Sounded like it might be a good fit for this. We should check that out." So, my name is Matt Lord and I a test maintainer. Sorry, I got to stay over here. I'm usually hand wavy so I got to get used to standing still. Um, and I work at planet scale. As far as what Vitess is, so Vitess is a cloudnative database. Uh, a a Kubernetes operator is a key part of the project. It's massively scalable and we'll talk about the details of what makes it so uh, highly available and MySQL compatible.

So what this means really what the value proposition is is that you have this scalable data layer which allows you to have virtually unlimited scaling of your data storage layer itself but also helps you scale your operations team. So the team of humans that are actually operating these systems and it gives the users of your systems whether they are internal or external the same user experience that they're used to with just a single MySQL instance. So the same MySQL that they would be using on their laptop or desktop for the development, they have that same type of experience when they're interfacing with your production uh data layer. On top of just being MySQL compatible and allowing you to scale, it has a lot of very nice features on top of that. So of course being able to shard and reshard your data. So once your data set reaches a point where it's very difficult, if not impossible at some point to manage that on a single machine, you start to partition that data. You create chunks of that data.

So you'll shard that data and then eventually you may need to reshard it. Maybe u maybe some of those shards can be combined, some of them need to be split and so on. So allows it gives you nice workflows in order to manage that. uh things like materializations. So materialized views of across this large distributed data set uh that's been that's managed by this massive cluster online schema changes. So
