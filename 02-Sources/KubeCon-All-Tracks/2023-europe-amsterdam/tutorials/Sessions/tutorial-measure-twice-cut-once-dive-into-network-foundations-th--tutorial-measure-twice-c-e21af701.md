---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Tutorials"
themes: ["Networking"]
speakers: ["Marino Wijay", "Jason Skrzypek", "Solo.io"]
sched_url: https://kccnceu2023.sched.com/event/1HyWa/tutorial-measure-twice-cut-once-dive-into-network-foundations-the-right-way-marino-wijay-jason-skrzypek-soloio
youtube_search_url: https://www.youtube.com/results?search_query=Tutorial%3A+Measure+Twice%2C+Cut+Once%3A+Dive+Into+Network+Foundations+the+Right+Way%21+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Tutorial: Measure Twice, Cut Once: Dive Into Network Foundations the Right Way! - Marino Wijay & Jason Skrzypek, Solo.io

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Tutorials]]
- Temas: [[Networking]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Marino Wijay, Jason Skrzypek, Solo.io
- Schedule: https://kccnceu2023.sched.com/event/1HyWa/tutorial-measure-twice-cut-once-dive-into-network-foundations-the-right-way-marino-wijay-jason-skrzypek-soloio
- Busca YouTube: https://www.youtube.com/results?search_query=Tutorial%3A+Measure+Twice%2C+Cut+Once%3A+Dive+Into+Network+Foundations+the+Right+Way%21+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Tutorial: Measure Twice, Cut Once: Dive Into Network Foundations the Right Way!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyWa/tutorial-measure-twice-cut-once-dive-into-network-foundations-the-right-way-marino-wijay-jason-skrzypek-soloio
- YouTube search: https://www.youtube.com/results?search_query=Tutorial%3A+Measure+Twice%2C+Cut+Once%3A+Dive+Into+Network+Foundations+the+Right+Way%21+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=3BLwRDh9JgA
- YouTube title: Tutorial: Measure Twice, Cut Once: Dive Into Network Foundations the Right Way! - Wijay & Skrzypek
- Match score: 0.989
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/tutorial-measure-twice-cut-once-dive-into-network-foundations-the-righ/3BLwRDh9JgA.txt
- Transcript chars: 87732
- Keywords: network, address, actually, server, command, networking, information, addresses, container, communicate, traffic, bridge, interface, containers, routing, little, basically, another

### Resumo baseado na transcript

so welcome to our Network foundation's Workshop one of the reasons we built this Workshop was because we felt that there was a massive gap between zero to understanding kubernetes networking so we wanted to fill those gaps for y'all and really help you understand you know all those different pieces and layers that add up together to allow you to do kubernetes networking but I had personal motivations too because when I joined solo the company I currently work for I actually you know struggled with learning istio the much time on this because this is the functionality of kubernetes this is why we're we've chosen to use this distributed system the next level on top of that going back to the DNS talks about being able to address things without having to manually to access workloads there's some some examples in here on how you would leverage it the fact that it is in fact using ibtables and DNS in this case and once again we can see the the magic DNS that's available through kubernetes there's also

### Excerpt da transcript

so welcome to our Network foundation's Workshop one of the reasons we built this Workshop was because we felt that there was a massive gap between zero to understanding kubernetes networking so we wanted to fill those gaps for y'all and really help you understand you know all those different pieces and layers that add up together to allow you to do kubernetes networking but I had personal motivations too because when I joined solo the company I currently work for I actually you know struggled with learning istio the service mesh but as I started to dig a little bit deeper and relate these Concepts back to some of the stuff that I used to do back in my network engineering days I started to map out how this would all flow and so you know my partner in crime here Jason allowed me to you know work with him to build This brilliant Workshop so I really hope you all enjoy it I'll go ahead and introduce myself my name is Marina wijay I'm a developer platform Advocate at solo so I work with the community I you know go out to conferences deliver a lot of talks and workshops while also just engaging with the community to understand what their needs are and through you know understanding and asking what they needed I found out it was networking you know give us the foundations so we can better understand how to use a container networking interface how to do service mesh and everything in between answers myself my name is Jason schepck I also work at solo I'm a field engineer based out of Buffalo New York um and the one thing I'll say right now is that we all have different Journeys to get into kubernetes or how we got to where we are basically today um and so hopefully the networking foundations will kind of establish a good foundation to uh so that we can all communicate freely about networking Concepts fantastic all right so I want you all to go to that QR code if you plan on participating in this Workshop you have a Sandbox environment waiting for you so head over there or you can even use a tiny URL to get to that solo Academy link once you're there feel free to launch the environment we're going to launch it actually I should I should have launched it right now I don't know what I was doing I'll go ahead and kick mine off mine looks a little different because I'm just using the back end version of the the version you're using which is the same thing so no big deal and so yeah I'll give you a couple a minute to just grab that and go ahead and start the workshop to
