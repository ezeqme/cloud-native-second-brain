---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Project Opportunities"
themes: ["Security", "SRE Reliability"]
speakers: []
sched_url: https://kccnceu2024.sched.com/event/1aQhB/achieving-balance-between-security-and-performance-in-falco-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=Achieving+Balance+Between+Security+and+Performance+in+Falco+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Achieving Balance Between Security and Performance in Falco | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Security]], [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: N/A
- Schedule: https://kccnceu2024.sched.com/event/1aQhB/achieving-balance-between-security-and-performance-in-falco-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=Achieving+Balance+Between+Security+and+Performance+in+Falco+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Achieving Balance Between Security and Performance in Falco | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1aQhB/achieving-balance-between-security-and-performance-in-falco-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=Achieving+Balance+Between+Security+and+Performance+in+Falco+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Ct4jOCKsy5o
- YouTube title: Achieving Balance Between Security and Performance in Falco | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/achieving-balance-between-security-and-performance-in-falco-project-li/Ct4jOCKsy5o.txt
- Transcript chars: 6302
- Keywords: course, kernel, security, performance, maintainer, balance, around, everything, person, maintainers, actually, container, basically, contributor, events, detections, detect, installing

### Resumo baseado na transcript

all right thank you everyone for joining my lightning talk about Falco I'll be talking about achieving balance between security and performance in our software so first of all uh some some of you here that have met are cncf maintainers so you have probably heard of Falco but in general what it is in couple words it's an open- source security solution for threat detection so we do runtime threat detection for your clusters hosts and kubernetes and very importantly Falco is now actually used by a lot of

### Excerpt da transcript

all right thank you everyone for joining my lightning talk about Falco I'll be talking about achieving balance between security and performance in our software so first of all uh some some of you here that have met are cncf maintainers so you have probably heard of Falco but in general what it is in couple words it's an open- source security solution for threat detection so we do runtime threat detection for your clusters hosts and kubernetes and very importantly Falco is now actually used by a lot of people in the community a lot of people that use cncf project and in fact this year Falco became a cncf graduated project so if you have never use Falco kind of what does it look like it's it's a magic box you put some rules inside that magic box that is exactly what you want to be alerted about so for example here we have a rule for a terminal sh shell in a container so I want to understand if that specific thing spawns in my cluster and then I put the rule and of course you can download our pre-made rules if you don't want to write your own put it in the magic box and outome alerts whenever these things happen but uh you don't just want to see a blank screen but yeah now it's not a blank screen so what is going to happen is that the Falco doesn't just give you an alert it basically tells you a lot of context around the alert so if you have our shell we can know everything about the container we know about kubernetes namespace process ancestors really a lot of things you have hundreds of fields to choose from to to have your alerts but what if you're a maintainer if you're a maintainer if you're a contributor which I hope uh some people will want to be uh you see FAL a little bit differently so first of all there's this thing that's called a kernel module or an ebpf probe this is the part that the user doesn't really want don't want to care about that but it's there in order to take those events from the kernel and then send them to the user space agent which is actually able to compute the rules and reach them with a lot of user space data kubernetes and many other things this is a very nice and flexible and extensible architecture but of course as a maintainer you will see that this Duality between kernel and user space is something that you have to really be uh to care about and sometimes as a users as well so imagine if you were a FAL container or contributor for a day what is it and now you're going around cubec con what is it that people will be asking
