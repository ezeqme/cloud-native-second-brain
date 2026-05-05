---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "101 Track"
themes: ["Security", "Storage Data", "Kubernetes Core"]
speakers: ["Ellen Körbes", "Tilt", "Tabitha Sable", "Datadog"]
sched_url: https://kccnceu2021.sched.com/event/iE3I/hacking-into-kubernetes-security-for-beginners-ellen-korbes-tilt-tabitha-sable-datadog
youtube_search_url: https://www.youtube.com/results?search_query=Hacking+into+Kubernetes+Security+for+Beginners+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Hacking into Kubernetes Security for Beginners - Ellen Körbes, Tilt & Tabitha Sable, Datadog

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[101 Track]]
- Temas: [[Security]], [[Storage Data]], [[Kubernetes Core]]
- País/cidade: Virtual / Virtual
- Speakers: Ellen Körbes, Tilt, Tabitha Sable, Datadog
- Schedule: https://kccnceu2021.sched.com/event/iE3I/hacking-into-kubernetes-security-for-beginners-ellen-korbes-tilt-tabitha-sable-datadog
- Busca YouTube: https://www.youtube.com/results?search_query=Hacking+into+Kubernetes+Security+for+Beginners+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Hacking into Kubernetes Security for Beginners.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE3I/hacking-into-kubernetes-security-for-beginners-ellen-korbes-tilt-tabitha-sable-datadog
- YouTube search: https://www.youtube.com/results?search_query=Hacking+into+Kubernetes+Security+for+Beginners+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=mLsCm9GVIQg
- YouTube title: Hacking into Kubernetes Security for Beginners - Ellen Körbes, Tilt & Tabitha Sable, Datadog
- Match score: 0.777
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/hacking-into-kubernetes-security-for-beginners/mLsCm9GVIQg.txt
- Transcript chars: 19219
- Keywords: controller, security, server, logs, admission, container, cluster, around, control, running, allowed, cuddle, namespace, environment, network, whatever, vulnerability, policy

### Resumo baseado na transcript

ah okay um new day new project time to write some code then i'm going to connect my local tooling to my development cluster and then i can get started i'm gonna do cube cuddle apply my um my usual tooling let's see oh wait what uh no part part something so let's let me do this by hand fail to create node parts the parts already allocated okay so someone's playing with my cluster parts i i told everyone 31337 that's me don't mess around with it gosh darn

### Excerpt da transcript

ah okay um new day new project time to write some code then i'm going to connect my local tooling to my development cluster and then i can get started i'm gonna do cube cuddle apply my um my usual tooling let's see oh wait what uh no part part something so let's let me do this by hand fail to create node parts the parts already allocated okay so someone's playing with my cluster parts i i told everyone 31337 that's me don't mess around with it gosh darn it okay who did this let's see who's around okay there's a lot of people here what are they doing i don't know i can't look at it can i look at them one by one no i can't okay so maybe there's some security in place here uh and i can't see what everyone else is doing okay you know what i'm not calling the security people they are not fun i'll i'll do this on my own um let me check something out here i remember seeing something funny in the onboarding documents so i was looking around the docs and i found this dav database controller so the controller creates new database instances pre-populated with fake data for use in dev environments it hangs often you can exact into the pod and if it's really wedged you can restart the process by deleting and recreating the pod and someone said something here about fixing our back privileges okay so we're using our back and our back is that thing where i have some permissions there's some things i can do in the cluster and there are some things i can't apparently i can't look at what my friends are doing to figure out who's messing with my stuff but if they set our back incorrectly which is very easy to do because it's convenient to set it incorrectly then maybe i can use that cascading effect where i am allowed to do some things i'm not allowed to do others but through the things i am allowed to do i can go around and manage to do the things i'm not allowed to do just in a very roundabout way so let's try that so we're looking at a dev database controller let's let's see if we can find that what can i do normally let's see keep cuddle off can i so i can do whatever i want in my own namespace but when i try to look at someone else's so let's see let's see what catherine's doing here when i try to look at someone else's namespace the stuff that i can do is very little almost nothing let's check something out so let's look at what's going on again and i have this dev environment controller i should be able to create pods in it yeah the documentation was right so for pods
