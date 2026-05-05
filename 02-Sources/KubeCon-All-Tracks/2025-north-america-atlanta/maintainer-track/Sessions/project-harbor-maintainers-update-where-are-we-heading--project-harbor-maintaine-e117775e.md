---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Orlin Vasilev", "SUSE", "Vadim Bauer", "8gears"]
sched_url: https://kccncna2025.sched.com/event/27Nn2/project-harbor-maintainers-update-where-are-we-heading-orlin-vasilev-suse-vadim-bauer-8gears
youtube_search_url: https://www.youtube.com/results?search_query=Project+Harbor+Maintainers+Update+-+Where+Are+We+Heading%3F+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Harbor Maintainers Update - Where Are We Heading? - Orlin Vasilev, SUSE & Vadim Bauer, 8gears

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Orlin Vasilev, SUSE, Vadim Bauer, 8gears
- Schedule: https://kccncna2025.sched.com/event/27Nn2/project-harbor-maintainers-update-where-are-we-heading-orlin-vasilev-suse-vadim-bauer-8gears
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Harbor+Maintainers+Update+-+Where+Are+We+Heading%3F+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Harbor Maintainers Update - Where Are We Heading?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Nn2/project-harbor-maintainers-update-where-are-we-heading-orlin-vasilev-suse-vadim-bauer-8gears
- YouTube search: https://www.youtube.com/results?search_query=Project+Harbor+Maintainers+Update+-+Where+Are+We+Heading%3F+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=PmBM9tEV_6U
- YouTube title: Project Harbor Maintainers Update - Where Are We Heading? - Orlin Vasilev & Vadim Bauer
- Match score: 0.886
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-harbor-maintainers-update-where-are-we-heading/PmBM9tEV_6U.txt
- Transcript chars: 24340
- Keywords: harbor, release, images, features, basically, feature, feedback, provider, satellite, update, updates, around, missing, create, policies, registry, provide, garbage

### Resumo baseado na transcript

Thank you for staying that late and uh I hope you had a great conference so far. I'm from SUSA obviously and I'm the community maintainer and that's Vadim uh one of the core maintainers of Project Harbor. Um about the security folks uh in the room the vulnerability scanning is still uh with uh we uh we use also 3y to create the sbomb you can export all the CVS from your images and your whole harbor instance or per project as well through the security hub. Um again quality uh quota and munability of the the uh images retention garbage collection and work rotation are super important for policy uh maintenance and and security perspective and yeah the robotic accounts are something that we're super happy to have and uh we So in the the previous release uh we rewrote the audit logs and uh you know to optimize for storage and also open up for other use cases so we can audit more things uh in the future. There is an a feature it's called active single active replication which allows you well which solves the problem if you have chron based replications scheduled very tightly let's say every couple of minutes you want to replicate data from another registry um and every

### Excerpt da transcript

Hello everyone and welcome to the harbor maintainers talk. Thank you for staying that late and uh I hope you had a great conference so far. My name is Orland. I'm from SUSA obviously and I'm the community maintainer and that's Vadim uh one of the core maintainers of Project Harbor. So we're going to try to do an overview what we've done for the last year. We're going to do some updates on community side and what comes next and uh Vadim is going to do some demos. So um how many of you are using harbor? I suppose most of you right um so I'm not going to read that um some very brief overview of how harbor how much harbor is um mature and that's the timeline 2014 uh initiated and at VMware 2016 open source 2018 uh donated and 2020 uh 2020 graduated at CNCF. So this year we celebrate something like 10 years. Depends how you look at it. Um if you missed that, I think we still have of these stickers. >> Oh yeah, we have. >> Yeah. So it's like our anniversary stickers and we're super happy to share that with you if you want to grab some.

Um so uh harbor superpowers uh for many uh harbor it's uh either in their home lab or they run it on enterprise but harbor has some some features that we think are distinguished through uh through the project from others like the arbback IDP and SSO uh um integration. Uh we can you can have your security folks happy uh by having all your images in place. you can replicate proxing and in recent um versions we added that vulnerability scanning sbomb generation and deployment policies um and also is for the ops right so you can automate uh almost everything right now uh with her uh and the claim is going to show that later you can do um the multi-tenency you can deploy hover with terapform palumi uh you have cola and policies all around so uh that's in a very uh brief the superpowers if you somehow missing them. Um a little bit deep dive on this uh the airbag and the project isolation so you can have a pure mute multi-tenency within harbor. Um the artifact distribution is like um a few mechanism how you can distribute artifacts by proxing preheating.

Um about the security folks uh in the room the vulnerability scanning is still uh with uh we uh we use also 3y to create the sbomb you can export all the CVS from your images and your whole harbor instance or per project as well through the security hub. You can take a look and deep dive into all that. Um again quality uh quota and munability of the the uh images retention garbage coll
