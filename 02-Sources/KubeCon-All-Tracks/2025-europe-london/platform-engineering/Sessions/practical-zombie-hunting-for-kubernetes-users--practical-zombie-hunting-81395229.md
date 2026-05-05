---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Holly Cummins", "Red Hat"]
sched_url: https://kccnceu2025.sched.com/event/1txGK/practical-zombie-hunting-for-kubernetes-users-holly-cummins-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Practical+Zombie+Hunting+for+Kubernetes+Users+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Practical Zombie Hunting for Kubernetes Users - Holly Cummins, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Holly Cummins, Red Hat
- Schedule: https://kccnceu2025.sched.com/event/1txGK/practical-zombie-hunting-for-kubernetes-users-holly-cummins-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Practical+Zombie+Hunting+for+Kubernetes+Users+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Practical Zombie Hunting for Kubernetes Users.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txGK/practical-zombie-hunting-for-kubernetes-users-holly-cummins-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Practical+Zombie+Hunting+for+Kubernetes+Users+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=1c2va5nATmQ
- YouTube title: Practical Zombie Hunting for Kubernetes Users - Holly Cummins, Red Hat
- Match score: 0.884
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/practical-zombie-hunting-for-kubernetes-users/1c2va5nATmQ.txt
- Transcript chars: 27466
- Keywords: servers, server, elasticity, utilization, zombie, pretty, actually, cluster, running, workload, switch, course, spreadsheet, nothing, called, support, though, capacity

### Resumo baseado na transcript

Uh my day job is that I help build Quarkus um which is cloudnative Java. Uh and so this talk is based on some of the things that I've seen in in when I was a consultant when I went that doesn't seem like a very good idea. And this matters a lot because if you have a server running at 12 to 18% of capacity, the cost to you for the hardware for the cloud is pretty much 100%. And again, you know, we can we can quantify how much this is costing us. So even if these things are running on renewable electricity, there's still a problem because every piece of hardware that we're wasting has what's called embodied carbon. And the zombie problem, you can call it the zombie problem, which sounds really exciting, or you can call it low utilization, which makes you sound a little bit more serious.

### Excerpt da transcript

So hello and welcome to the fun side of the climate apocalypse. Um I'm Holly Cumins. I work for Red Hat. Uh my day job is that I help build Quarkus um which is cloudnative Java. Uh but I have a past life as a consultant. Uh and so this talk is based on some of the things that I've seen in in when I was a consultant when I went that doesn't seem like a very good idea. Um so hands up if this is familiar. I get charged $2 a month from AWS and I'm too scared to turn it off and too lazy to figure out Yep. Yep. Yep. There's hands. Too lazy to figure out what's causing the bandwidth. Or I get emails from an eight-year-old WordPress install and I'm pretty sure it's an on-rem server, but I don't know where it is and I don't know what it is and I can't turn it off, but that thing is still emailing me. So, a few of you put your hands up. But of course, losing $2 a month to an AWS instance that you can't find, that's that's for amateurs really. The the leaders in our industry do it a bit better. So, here we have Twitter who managed to forget about 700 GPUs as one does.

I mean, hands up, who hasn't lost 700 GPUs because you just misplaced them? And the thing is, the thing that's so terrible about this story is GPUs are in demand. We all want GPUs. And there was 700 of them sat there powered up using power and not doing anything at all. And it's easy to laugh at this as something that happens to other people that other people do, but we have all done this. I in 2018, uh, I learned Kubernetes. And so I did what anybody learning new technology would do. I created a cluster, but I had a bit too much work in progress. So after creating the cluster, I forgot about the cluster that I'd created for two months. And then when I went back and looked at it, I realized that I'd created a fairly wellsp speced cluster. This thing was a,000 pounds a month. And it was just sat there doing nothing while I did my other jobs. So that was a slightly awkward conversation with my boss. And I I didn't learn from that experience. So, while I was preparing this talk, I had um a Mac server for Mac Stadium that I was using for Maxi, but I'd kind of not quite managed to make it work.

And then I'd got distracted doing other things like writing a talk. And then I went back and looked at it and it was £150 a month that again was just sat there burning CPU doing nothing. So, how how bad is this problem? Is it just, you know, a few quite isolated but kind of hilarious incidents like Twitter losing 70
