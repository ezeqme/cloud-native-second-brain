---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "101 Track"
themes: ["101 Track"]
speakers: ["Suneeta Mall", "Nearmap"]
sched_url: https://kccncna2021.sched.com/event/lV0P/who-killed-my-pod-#whodunit-suneeta-mall-nearmap
youtube_search_url: https://www.youtube.com/results?search_query=Who+Killed+My+Pod%3F+%23Whodunit+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Who Killed My Pod? #Whodunit - Suneeta Mall, Nearmap

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[101 Track]]
- Temas: [[101 Track]]
- País/cidade: United States / Los Angeles
- Speakers: Suneeta Mall, Nearmap
- Schedule: https://kccncna2021.sched.com/event/lV0P/who-killed-my-pod-#whodunit-suneeta-mall-nearmap
- Busca YouTube: https://www.youtube.com/results?search_query=Who+Killed+My+Pod%3F+%23Whodunit+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Who Killed My Pod? #Whodunit.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV0P/who-killed-my-pod-#whodunit-suneeta-mall-nearmap
- YouTube search: https://www.youtube.com/results?search_query=Who+Killed+My+Pod%3F+%23Whodunit+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=eH4x5PGgDoM
- YouTube title: Who Killed My Pod? #Whodunit - Suneeta Mall, Nearmap
- Match score: 0.792
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/who-killed-my-pod-whodunit/eH4x5PGgDoM.txt
- Transcript chars: 24426
- Keywords: container, memory, process, killed, actually, running, kernel, resource, getting, runtime, limits, processes, little, docker, saying, containers, talking, quality

### Resumo baseado na transcript

hi thank you for tuning in i am sunita mal i work as a director of ai model systems at mia map today we are going to talk about a peculiar kind of crime scene investigation this is cube csi and focus is who killed my part exactly who has done it every intriguing investigation begins with a disaster and ours is no different it started off by cube control apply my pixie dust magical app which is we thought is well tested in local environment and bare metal and

### Excerpt da transcript

hi thank you for tuning in i am sunita mal i work as a director of ai model systems at mia map today we are going to talk about a peculiar kind of crime scene investigation this is cube csi and focus is who killed my part exactly who has done it every intriguing investigation begins with a disaster and ours is no different it started off by cube control apply my pixie dust magical app which is we thought is well tested in local environment and bare metal and as soon as we deployed deployed excuse me all hell broke loose we started to see a container being killed left and right with om kill as a reason and error code exit code 137 and this is then going into crash loopback which is a pure joy to look at when you are getting things out into production so so then that sparked a massive hunt for what exactly happened and who killed the pot so let's start with the investigation bone we have a particular container process that's being killed repeatedly potentially uh because it's being a memory hogger now we know that the kill is a forceful brutal and it's killed with a sickle as a signal so it's either somebody in somebody with more power has killed the process without the the desired wishes and it's a runtime error then okay so we we know uh some context and let's look at the details for how the containers run on a host machine and then who are all in charge um in making the container process life cycle run on a host so we obviously have a host the the their metal or the instance or virtual and then on top we have the container runtime and container runtime is comprised of two different levels the lower level runtime and higher level and time the lower level deals with interacting with systems host using system calls and making use of kernel and os features container d which is the higher level runtime then deals with a higher level apis api that interfaces users and deals with image management etc aspects so then we have the runtime that's broken down into two levels low level and high level run c and container d are two very popular examples of these runtimes obviously there are many different other runtimes available too so now we have container on time and then your process that we call container then runs on top of it and the the layer underneath the runtime and the host then guarantees the isolation for your container process so they are kind of not stepping onto each other's toes so this is what happens on the host level now when we put kubernetes in th
