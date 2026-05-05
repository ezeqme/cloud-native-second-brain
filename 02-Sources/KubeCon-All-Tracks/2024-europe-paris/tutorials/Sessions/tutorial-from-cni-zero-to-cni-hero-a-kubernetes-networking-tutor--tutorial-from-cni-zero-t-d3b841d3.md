---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Tutorials"
themes: ["Networking", "Kubernetes Core"]
speakers: ["Doug Smith", "Tomofumi Hayashi", "Red Hat"]
sched_url: https://kccnceu2024.sched.com/event/1YeQ4/tutorial-from-cni-zero-to-cni-hero-a-kubernetes-networking-tutorial-using-cni-doug-smith-tomofumi-hayashi-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Tutorial%3A+From+CNI+Zero+to+CNI+Hero%3A+A+Kubernetes+Networking+Tutorial+Using+CNI+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Tutorial: From CNI Zero to CNI Hero: A Kubernetes Networking Tutorial Using CNI - Doug Smith & Tomofumi Hayashi, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Tutorials]]
- Temas: [[Networking]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Doug Smith, Tomofumi Hayashi, Red Hat
- Schedule: https://kccnceu2024.sched.com/event/1YeQ4/tutorial-from-cni-zero-to-cni-hero-a-kubernetes-networking-tutorial-using-cni-doug-smith-tomofumi-hayashi-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Tutorial%3A+From+CNI+Zero+to+CNI+Hero%3A+A+Kubernetes+Networking+Tutorial+Using+CNI+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Tutorial: From CNI Zero to CNI Hero: A Kubernetes Networking Tutorial Using CNI.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeQ4/tutorial-from-cni-zero-to-cni-hero-a-kubernetes-networking-tutorial-using-cni-doug-smith-tomofumi-hayashi-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Tutorial%3A+From+CNI+Zero+to+CNI+Hero%3A+A+Kubernetes+Networking+Tutorial+Using+CNI+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=YumoKGhuZ2o
- YouTube title: Tutorial: From CNI Zero to CNI Hero: A Kubernetes Networking Tutorial Using CNI
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/tutorial-from-cni-zero-to-cni-hero-a-kubernetes-networking-tutorial-us/YumoKGhuZ2o.txt
- Transcript chars: 42372
- Keywords: config, plugin, interface, configuration, create, address, container, result, plugins, actually, object, network, windows, output, course, command, version, standard

### Resumo baseado na transcript

hello okay let's start this tutorial sessions so this tutorial is about the cni from cni Z to cni Hero the kubernetes networking tutorial using cni I'm Tomi and and I'm Doug Smith so I'm tomashi working in the red hat and then works for the open shift engineering as well as the in upstream cni and M cni maintenance as well and join the network Plumping working group as well and I am Doug Smith I'm also a member of the network Plumbing working group uh Tomo and I between those two things and it really does seem like wow there's a lot of stuff here and it also can be since it has that history of um kind of predating kubernetes it's a different API and I think that sometimes people that are really accustomed to kubernetes take a look at it and they're like wow that is is more than I bargained for but it's not that hard um to get in there and once you start kind of picking it apart and making your own customizations

### Excerpt da transcript

hello okay let's start this tutorial sessions so this tutorial is about the cni from cni Z to cni Hero the kubernetes networking tutorial using cni I'm Tomi and and I'm Doug Smith so I'm tomashi working in the red hat and then works for the open shift engineering as well as the in upstream cni and M cni maintenance as well and join the network Plumping working group as well and I am Doug Smith I'm also a member of the network Plumbing working group uh Tomo and I both work together on multis cni which is a cni plugin that allows you to attach multiple network interfaces into pods and kubernetes um what tomo didn't mention is that Tomo's also created a number of other cni plugins such as ones that you you may might even take for granted like a static cni um cni plugins to override routes um and we've also I've also created another cni plugin called whereabouts which is for like a dynamic uh allocation of IP addresses so today what we're going to look at first is an intro to cni Tomo's going to walk you through everything about how cni Works um in the end really uh don't it might feel like a lot but really it's in the end it's really a few just simple things that you uh need to take a grasp of what we will do is we will be very comprehensive here with that in mind we're also going to walk you through configurations and all of the details and how you can actually configure cni Tomo's then going to take a glance over how you're going to develop cni plugins if you have an interest in that and as Tomo kind of noted uh originally is there are a number of slides that we have as reference material in the slides to download that uh we decided were maybe too much detail but they could be really useful for you when you go there um with that all in place since you've got the basics we're going to do a Hands-On tutorial um where uh you can follow along if you'd like download the deck there's a link to a um GitHub repository that's got configurations for kind and all of the resources that are used in there um there's also kind of a bit of a troubleshooting aspect to that and then I'll kind of um touch on that and last but not least we'll kind of show you how you can get linked up with the cni community and where all the resources are um with that being said I will let Tomo um kick it off with an intro into cni thank you D so let's cover the what the cni is first important stuff right so what the cni does for you is maybe the simply to say in case of the kubernetes cni pro
