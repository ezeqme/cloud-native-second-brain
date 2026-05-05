---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Security + Identity + Policy"
themes: ["Security"]
speakers: ["Lorenzo Fontana", "Sysdig"]
sched_url: https://kccnceu2021.sched.com/event/iE4t/the-art-of-hiding-yourself-lorenzo-fontana-sysdig
youtube_search_url: https://www.youtube.com/results?search_query=The+Art+of+Hiding+Yourself+CNCF+KubeCon+2021
slides: []
status: parsed
---

# The Art of Hiding Yourself - Lorenzo Fontana, Sysdig

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Security]]
- País/cidade: Virtual / Virtual
- Speakers: Lorenzo Fontana, Sysdig
- Schedule: https://kccnceu2021.sched.com/event/iE4t/the-art-of-hiding-yourself-lorenzo-fontana-sysdig
- Busca YouTube: https://www.youtube.com/results?search_query=The+Art+of+Hiding+Yourself+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre The Art of Hiding Yourself.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE4t/the-art-of-hiding-yourself-lorenzo-fontana-sysdig
- YouTube search: https://www.youtube.com/results?search_query=The+Art+of+Hiding+Yourself+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Ti5Uj984CLY
- YouTube title: The Art of Hiding Yourself - Lorenzo Fontana, Sysdig
- Match score: 0.773
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/the-art-of-hiding-yourself/Ti5Uj984CLY.txt
- Transcript chars: 17221
- Keywords: process, cluster, access, processes, machine, actually, hiding, container, library, everything, myself, either, always, directly, itself, create, network, basically

### Resumo baseado na transcript

hello everyone um this is the art of ident yourself and i'm lorenzo fontana uh i work as an open source software engineer at cystic where i am mainly focused on the clcf project alco which is the project for container runtime security i'm the author of linux observability with bpf with david and today i want to you know put the attention on something that we always do that we never think about which is closing the doors right we continue closing doors putting firewalls um doing all the

### Excerpt da transcript

hello everyone um this is the art of ident yourself and i'm lorenzo fontana uh i work as an open source software engineer at cystic where i am mainly focused on the clcf project alco which is the project for container runtime security i'm the author of linux observability with bpf with david and today i want to you know put the attention on something that we always do that we never think about which is closing the doors right we continue closing doors putting firewalls um doing all the prevention all the putting our system in a state where we feel like it's secure because security is a feeling right you always put in place mechanisms put in place uh you know redulify system rootless containers everything your power and that's very good to do but you never know if tomorrow someone has a zero day on the kernel on the software that you use on your bull loader on some hardware that you're running right so i think that you should be always prepared for what happens if someone breaks in let's do an analogy with your house you're in your house you have the biggest door in the market you have always you know all the windows are gated everything but if someone breaks in and they find a way to breaking without passing through like they come from the roof or whatever they are there they might do a lot of mess or whatever they might spend their time you know getting all your stuff and doing a big mess but what if they don't it gets worse right because let's say that they just that they are just in and they don't do anything they just you know sit in a car and wait for you to go to sleep you know it sounds scary but that's what people usually want to do with your clusters they usually don't go in there and start being very loud they go in there and they want to be as hidden as possible and they want to be catched so that they can maximize their profit let me play this role now i'm lorenzo i'm not an open source software engineer assisting anymore for the next 10 minutes and i will be the person trying to hide this is my new vest with my mask and everything like not the face mask but the ice mask and i want to be in a position where i have a cluster that i already compromised i have let's say a zero day kubernetes i am in the cluster and my duty is to minimize the risk i don't want to be discovered while maximize the profit of you know getting access to other machines in the cluster and i don't want to specifically be discovered because getting access to the machine cos
