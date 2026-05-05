---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Maintainer Track"
themes: ["AI ML", "Runtime Containers", "Community Governance"]
speakers: ["Phil Estes", "AWS", "Mike Brown", "IBM", "Maksym Pavlenko", "Apple", "Michael Zappa", "Microsoft"]
sched_url: https://kccncna2022.sched.com/event/182MQ/a-containerd-and-friends-update-whats-new-in-runtimes-phil-estes-aws-mike-brown-ibm-maksym-pavlenko-apple-michael-zappa-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=A+Containerd+And+Friends+Update%3A+What%E2%80%99s+New+In+Runtimes%3F+CNCF+KubeCon+2022
slides: []
status: parsed
---

# A Containerd And Friends Update: What’s New In Runtimes? - Phil Estes, AWS; Mike Brown, IBM; Maksym Pavlenko, Apple; Michael Zappa, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Community Governance]]
- País/cidade: United States / Detroit
- Speakers: Phil Estes, AWS, Mike Brown, IBM, Maksym Pavlenko, Apple, Michael Zappa, Microsoft
- Schedule: https://kccncna2022.sched.com/event/182MQ/a-containerd-and-friends-update-whats-new-in-runtimes-phil-estes-aws-mike-brown-ibm-maksym-pavlenko-apple-michael-zappa-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=A+Containerd+And+Friends+Update%3A+What%E2%80%99s+New+In+Runtimes%3F+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre A Containerd And Friends Update: What’s New In Runtimes?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182MQ/a-containerd-and-friends-update-whats-new-in-runtimes-phil-estes-aws-mike-brown-ibm-maksym-pavlenko-apple-michael-zappa-microsoft
- YouTube search: https://www.youtube.com/results?search_query=A+Containerd+And+Friends+Update%3A+What%E2%80%99s+New+In+Runtimes%3F+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=QQGoTcgvz2s
- YouTube title: A Containerd And Friends Update: What’s New...Phil Estes, Mike Brown, Maksym Pavlenko, Michael Zappa
- Match score: 0.738
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/a-containerd-and-friends-update-whats-new-in-runtimes/QQGoTcgvz2s.txt
- Transcript chars: 27716
- Keywords: container, sandbox, actually, containers, docker, support, around, release, working, continuity, network, images, interface, called, containerdy, updates, everything, plugin

### Resumo baseado na transcript

we've I I hope you're here because you're interested in container D but we've actually called it the containerdy and Friends update because we have quite a few sub projects now that I know many are interested in um who who was able to be in the Keynotes and see Derek McGowan give our video update I was pretty cool to have Derek involved he's got a new baby at home so he couldn't be here this year A lot of times he and I have been tag teaming this

### Excerpt da transcript

we've I I hope you're here because you're interested in container D but we've actually called it the containerdy and Friends update because we have quite a few sub projects now that I know many are interested in um who who was able to be in the Keynotes and see Derek McGowan give our video update I was pretty cool to have Derek involved he's got a new baby at home so he couldn't be here this year A lot of times he and I have been tag teaming this talk but I'm always amazed that uh people still come to hear about continuity it's like inviting a bunch of friends over and having a plumber come talk about the plumbing in your house and how interesting the pipes are but you know we're we're a pretty core foundational uh run time but but maybe not super exciting in the sense of like tons of new features but we're going to try and cover a little bit about where the project is going you heard from Derek if you saw that video kind of our release cycle updates so there's four of us here it's going to move a little bit quick I'm just going to give the intro some of the community and release updates uh and then you can see we've got uh Maxim Michael Zappa and Mike Brown we're all maintainers of the project as well as many others um who are even some here in the room and so uh hopefully if if we don't cover the thing you're interested in you can find us after the talk you can find us around this week uh grab us and take us to the sponsor showcase and find a seat and we'd love to chat about anything you're interested in so as I said I'm going to kind of Rapid Fire go through a few hopefully interesting updates one is that we currently have we're about to have three uh release lines uh under development one five would-be end of life but we've just extended that into January so a few more months and we just made a release to catch a few back ports of bug fixes so folks that are still using one five there's still a few months of support for that uh 1 6 is kind of the biggest news um we just made a readme update and I have a slide about that in a minute but we just uh made our latest release just a few days ago of 1.6 uh that's probably kind of the the most stable and used uh version of containerdy at the moment that's what a lot of projects are importing and then of course there's our main branch where we've been working towards our one seven release and we just released the beta zero for that yesterday uh Derek mentioned that in his video um and so that's where a lot of t
