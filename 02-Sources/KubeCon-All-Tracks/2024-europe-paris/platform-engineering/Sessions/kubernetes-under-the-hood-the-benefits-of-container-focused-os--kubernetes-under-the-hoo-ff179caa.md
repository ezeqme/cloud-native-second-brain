---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Platform Engineering"
themes: ["AI ML", "Platform Engineering", "Runtime Containers", "Kubernetes Core"]
speakers: ["Mathieu Tortuyaux", "Microsoft", "Timothée Ravier", "Red Hat"]
sched_url: https://kccnceu2024.sched.com/event/1YePg/kubernetes-under-the-hood-the-benefits-of-container-focused-os-mathieu-tortuyaux-microsoft-timothee-ravier-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+Under+the+Hood%3A+The+Benefits+of+Container+Focused+OS+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Kubernetes Under the Hood: The Benefits of Container Focused OS - Mathieu Tortuyaux, Microsoft & Timothée Ravier, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Runtime Containers]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Mathieu Tortuyaux, Microsoft, Timothée Ravier, Red Hat
- Schedule: https://kccnceu2024.sched.com/event/1YePg/kubernetes-under-the-hood-the-benefits-of-container-focused-os-mathieu-tortuyaux-microsoft-timothee-ravier-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+Under+the+Hood%3A+The+Benefits+of+Container+Focused+OS+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Kubernetes Under the Hood: The Benefits of Container Focused OS.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YePg/kubernetes-under-the-hood-the-benefits-of-container-focused-os-mathieu-tortuyaux-microsoft-timothee-ravier-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+Under+the+Hood%3A+The+Benefits+of+Container+Focused+OS+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Kp6FXsIpPBs
- YouTube title: Kubernetes Under the Hood: The Benefits of Container Focused OS- Mathieu Tortuyaux & Timothée Ravier
- Match score: 0.865
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/kubernetes-under-the-hood-the-benefits-of-container-focused-os/Kp6FXsIpPBs.txt
- Transcript chars: 26484
- Keywords: container, ignition, configuration, containers, updates, version, operating, channel, projects, reboot, cluster, little, everything, update, butane, feature, instance, provider

### Resumo baseado na transcript

hi everyone we are super excited to be here with you today to talk about container operating systems um the goal of this presentation of this session of today's session is to give you the key elements to get started with container rest so we are going to introduce some low-level elements uh technical implementation and stuff like that but also high level concept uh to understand container race the goal of this session is to give you the key elements and to understand why you should use container rest

### Excerpt da transcript

hi everyone we are super excited to be here with you today to talk about container operating systems um the goal of this presentation of this session of today's session is to give you the key elements to get started with container rest so we are going to introduce some low-level elements uh technical implementation and stuff like that but also high level concept uh to understand container race the goal of this session is to give you the key elements and to understand why you should use container rest to operate your container workloads so before going further let me quickly introduce myself uh my name is mat I work as a flat car engineer inside Microsoft uh I mainly involved in the test automation of flat car I'm involved on feature development and transversal topics like for example cluster API or Upstream contributions to over projects in the Linux ecosystems and outside of work I co-funded the S FRS Association so with my friend we here to organize develops and S events in France meetups and also bigger events like the S Summer Camp which is a two-day event where we organize uh talks and stuff like that around devops topics and what about you timot hey thanks B for the introduction so I'm Timo ravier and I'm currently working as a chorus engineer at rad so I work on F chus and rad for S mly uh and then on the side in the community I work a lot in the feder community especially on the feder atomic desktops we just went through rebranding we were used to call Fed silver blue fed kinoite and all of those variants and now we call them all the photo Atomic desktops uh and I also uh do some work on the KD side KD developer working on Discover and other applications all right enough about us let's talk about before setting up a little bit of context of why we're here and why we're bothering talking about continer Focus OES so we're here to run applications here with the entire conference is about cucon Cloud native Native apps uh running application inside of containers and pushing them somewhere to run them to get a service out to users to get a service to our Enterprise to sell or to customers or to clients and so those applications we now we run them mostly on containers and we need a platforms to run them to deploy our containers to make sure they are okay to make sure they run well to monitor them to ensure security all those things and so well we are copon so here obviously we're going to look at kubernetes and how to how all of this fits in and so yeah
