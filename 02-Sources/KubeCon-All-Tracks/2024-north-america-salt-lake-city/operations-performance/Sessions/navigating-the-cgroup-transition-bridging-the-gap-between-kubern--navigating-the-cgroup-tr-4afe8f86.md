---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Operations + Performance"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Sohan Kunkerkar", "Red Hat Inc"]
sched_url: https://kccncna2024.sched.com/event/1i7nI/navigating-the-cgroup-transition-bridging-the-gap-between-kubernetes-and-user-expectations-sohan-kunkerkar-red-hat-inc
youtube_search_url: https://www.youtube.com/results?search_query=Navigating+the+Cgroup+Transition%3A+Bridging+the+Gap+Between+Kubernetes+and+User+Expectations+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Navigating the Cgroup Transition: Bridging the Gap Between Kubernetes and User Expectations - Sohan Kunkerkar, Red Hat Inc

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Sohan Kunkerkar, Red Hat Inc
- Schedule: https://kccncna2024.sched.com/event/1i7nI/navigating-the-cgroup-transition-bridging-the-gap-between-kubernetes-and-user-expectations-sohan-kunkerkar-red-hat-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Navigating+the+Cgroup+Transition%3A+Bridging+the+Gap+Between+Kubernetes+and+User+Expectations+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Navigating the Cgroup Transition: Bridging the Gap Between Kubernetes and User Expectations.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7nI/navigating-the-cgroup-transition-bridging-the-gap-between-kubernetes-and-user-expectations-sohan-kunkerkar-red-hat-inc
- YouTube search: https://www.youtube.com/results?search_query=Navigating+the+Cgroup+Transition%3A+Bridging+the+Gap+Between+Kubernetes+and+User+Expectations+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Ho2_aBr08OE
- YouTube title: Navigating the Cgroup Transition: Bridging the Gap Between Kubernetes and User Expec... S. Kunkerkar
- Match score: 0.988
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/navigating-the-cgroup-transition-bridging-the-gap-between-kubernetes-a/Ho2_aBr08OE.txt
- Transcript chars: 32874
- Keywords: memory, cgroup, container, resource, actually, kernel, already, understand, specific, resources, support, limits, feature, basically, process, features, behind, started

### Resumo baseado na transcript

I hope you are having a great time at cubec con and enjoy some interesting sessions over the last 2 days and I'm hoping today you're going to enjoy the same um thank you for joining me today kubernetes is complex and it takes a lot of U you know challenges to uh build something behind the scenes and one of the components that is actually using that is Linux C group the backbone behind the container resource control that limits and prioritizes CPU dis and memory if you ever uh to to see the container specific metrics so I've already created uh Cube curle proxy behind the scenes so um that ID is already there I'm just going ahead and kind of uh quering that so what you see here is the same thing what uh when you go inside CFS C group and uh trying to kind of go through each and every file to look for the values so this is the easiest way to query any metrics rather than going inside uh C group uh files right cool so with this demo um let's understand now we know about cgroup in kubernetes let's understand uh the benefits of cgroup V2 in uh kubernetes uh we talked about uh memory Q in the previous slide but let's discuss what that means uh for uh kubernetes so it allows for fine Grand allocation memory allocation so what kubernetes does is like it basically um prioritizes memory for critical applications and uh it reduces the risk for um slowdowns or crashes uh in essential...

### Excerpt da transcript

I hope you are having a great time at cubec con and enjoy some interesting sessions over the last 2 days and I'm hoping today you're going to enjoy the same um thank you for joining me today kubernetes is complex and it takes a lot of U you know challenges to uh build something behind the scenes and one of the components that is actually using that is Linux C group the backbone behind the container resource control that limits and prioritizes CPU dis and memory if you ever wonder uh why your uh container you know gets um killed despite setting the memory limits or why CPU uh gets you know uh because of uh thing where you feel like you know it's getting out of control you might be uh come across thing called uh cgroups which is impacting your applications so in today's sessions we going to talk about something which is really important uh for someone who is working with kubernetes that is transition from C group V1 to V2 that shift will impact the resource management uh performance and the the resource control and uh the workload compatibility so a little bit about myself uh my name is soan kerker I work at Red Hat as a senior software engineer I'm one of the cryo maintainers and a member of Sig node which works predominantly on uh cuate uh and node specific projects if I'm not working I'll be either playing flute or enjoying tracking and outdoor activities so um here's the agenda for today's talk we'll be uh covering the first part where we'll talking about the foundation of C group followed by the migration process and in the second half we'll talk about the impact while doing the transition and think about the future outlook so can I get a quick show off hands how many of you are using cgroup V2 in their production clusters that's good and how about V1 all right so uh with this talk my intention is uh towards the end of this session I can pursue towards moving to V2 so let's get started so uh uh before that I want to make sure that we are on the same page so I we'll quickly touch base on what is cgroup exactly cgroup is a Linux kernel feature that manages the system resources so you can actually uh see now you can control the CPU memory and dis IO for for the process C group you can imagine as it can actually uh you know um impose the limit on the resource usage at the same time it can monitor uh the performance of the group resources and also controls the scheduling and prioritization one of the important part of uh C group is it doesn't allow any singl
