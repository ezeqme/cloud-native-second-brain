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
themes: ["Platform Engineering"]
speakers: ["Alexander Perlman", "Narayanamurthi Mari", "Capital One"]
sched_url: https://kccnceu2025.sched.com/event/1tx7E/a-fork-to-reckon-with-minimizing-friction-when-adopting-oss-alexander-perlman-narayanamurthi-mari-capital-one
youtube_search_url: https://www.youtube.com/results?search_query=A+Fork+to+Reckon+With%3A+Minimizing+Friction+When+Adopting+OSS+CNCF+KubeCon+2025
slides: []
status: parsed
---

# A Fork to Reckon With: Minimizing Friction When Adopting OSS - Alexander Perlman & Narayanamurthi Mari, Capital One

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: United Kingdom / London
- Speakers: Alexander Perlman, Narayanamurthi Mari, Capital One
- Schedule: https://kccnceu2025.sched.com/event/1tx7E/a-fork-to-reckon-with-minimizing-friction-when-adopting-oss-alexander-perlman-narayanamurthi-mari-capital-one
- Busca YouTube: https://www.youtube.com/results?search_query=A+Fork+to+Reckon+With%3A+Minimizing+Friction+When+Adopting+OSS+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre A Fork to Reckon With: Minimizing Friction When Adopting OSS.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx7E/a-fork-to-reckon-with-minimizing-friction-when-adopting-oss-alexander-perlman-narayanamurthi-mari-capital-one
- YouTube search: https://www.youtube.com/results?search_query=A+Fork+to+Reckon+With%3A+Minimizing+Friction+When+Adopting+OSS+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=yeg-uoBYCO0
- YouTube title: A Fork to Reckon With: Minimizing Friction When Adopting... Alexander Perlman & Narayanamurthi Mari
- Match score: 0.817
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/a-fork-to-reckon-with-minimizing-friction-when-adopting-oss/yeg-uoBYCO0.txt
- Transcript chars: 31477
- Keywords: mutation, policy, resources, source, create, basically, internal, solution, manifest, mutate, specific, contribution, inject, working, containers, dependencies, underlying, server

### Resumo baseado na transcript

But before we tell you what it is and how to protect yourselves, let us tell you a little bit about who we are. I'm also a QFlow uh member and contributor and I'm deeply honored to be here today as a speaker and I'm also honored to be sharing the stage with Mory. So, the point I'm trying to make is for the love of all that is good and holy, please, please, please resist the alert of NIH and use industry standard open source software instead. So when you work in a regulated industry like we do where there are elevated security requirements and regulatory requirements, sometimes you can't just use the open source software that you want to use off the shelf. Now, granted, on some level, Kubernetes is kind of at the end of the bell curve, but you get the idea. And, uh, it's a real privilege to collaborate with people from all over the world and learn from them and develop your craft and develop friendships.

### Excerpt da transcript

Okay. Hi everybody. We're here today to save you from an unspeakable evil. But before we tell you what it is and how to protect yourselves, let us tell you a little bit about who we are. the pond for a couple of days by myself and I work at Capital One. Um, I help maintain a machine learning platform internally. I'm also a QFlow uh member and contributor and I'm deeply honored to be here today as a speaker and I'm also honored to be sharing the stage with Mory. Thank you, Alex. Hi everyone, my name is Morty. I work as a distinguished engineer in Capital Oneman. I'm passionate about open-source Kubernetes building platforms and related services. I also come from New York City and I live in New Jersey again along with my amazing wife and two kids. Uh it is exciting and I'm feeling great to be here to present this topic along with Alex who is a true subject matter expert in this area. Thank you Matthew. So as I was saying we're here to protect you from an unspeakable evil. If I could add an ominous sound effect to the slide, I would, but you'll just have to use your imagination.

If you're not familiar with this acronym, congratulations. May you never see the horrors that we've borne witness to. NIH stands for not invented here. And it's basically when companies decide to roll their own solutions instead of leveraging mature industry standard, widely adopted open source solutions. To be clear, there are specific use cases where it makes sense to build versus buy or whatever the open source equivalent of that is. I guess build versus don't buy. Um, so a little context on this image here. Um, we're not allowed to use unlicensed images in our deck. So in the spirit of malicious compliance, uh, I asked my children and Morphe asked his children to illustrate some of the memes we wanted to use. So you'll see sprinkle throughout this uh presentation some drawings. Uh and if you're not familiar with this, this is from Monty Python and the Holy Grail. It's one of the knights who say NI. I don't know how to pronounce NIH, but I'm just going to call it NI from now on. U so kudos to our to our children for helping us out.

So uh story time. At one of my earliest jobs within the industry, I was tasked with maintaining uh an in-house version of Terraform implemented in Ruby of all things. And it was kind of a nightmare. And on some level, the rest of my career since then has been a kind of prolonged horrified recoil to that experience. At some point, I asked for advice abo
