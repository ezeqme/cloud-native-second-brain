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
themes: ["AI ML", "Storage Data", "SRE Reliability", "Community Governance"]
speakers: ["Maciej Szulik", "Defense Unicorns", "Janet Kuo", "Google"]
sched_url: https://kccncna2025.sched.com/event/27Nmt/managing-data-at-scale-best-practices-and-evolution-of-sig-apps-maciej-szulik-defense-unicorns-janet-kuo-google
youtube_search_url: https://www.youtube.com/results?search_query=Managing+Data+at+Scale%3A+Best+Practices+and+Evolution+of+SIG-Apps+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Managing Data at Scale: Best Practices and Evolution of SIG-Apps - Maciej Szulik, Defense Unicorns & Janet Kuo, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Storage Data]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Maciej Szulik, Defense Unicorns, Janet Kuo, Google
- Schedule: https://kccncna2025.sched.com/event/27Nmt/managing-data-at-scale-best-practices-and-evolution-of-sig-apps-maciej-szulik-defense-unicorns-janet-kuo-google
- Busca YouTube: https://www.youtube.com/results?search_query=Managing+Data+at+Scale%3A+Best+Practices+and+Evolution+of+SIG-Apps+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Managing Data at Scale: Best Practices and Evolution of SIG-Apps.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Nmt/managing-data-at-scale-best-practices-and-evolution-of-sig-apps-maciej-szulik-defense-unicorns-janet-kuo-google
- YouTube search: https://www.youtube.com/results?search_query=Managing+Data+at+Scale%3A+Best+Practices+and+Evolution+of+SIG-Apps+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9xpp3wvoSDg
- YouTube title: Managing Data at Scale: Best Practices and Evolution of SIG-Apps - Maciej Szulik & Janet Kuo
- Match score: 0.92
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/managing-data-at-scale-best-practices-and-evolution-of-sig-apps/9xpp3wvoSDg.txt
- Transcript chars: 19810
- Keywords: particular, working, stateful, deployment, actually, controller, entire, workloads, talking, workload, controllers, already, single, basically, examples, probably, little, failed

### Resumo baseado na transcript

Today we're going to talk about managing data at scale best practices and evolution of sik apps. We focus on application user experience including the experience for app developers and app operators. Uh because um as you probably noticed a lot of the work that we do and the Kubernetes enhancements proposals the cap they the majority of them have fourdigit number. that was actually in the deployment controller specifically and the reason that I'm telling that is because this particular enhancement uh that Philip who's sitting in the first the second row um is working and pushing hard but the problem with that is so the The problem with that is that because the changes coming from that that particular change are spanning the entire deployment and replica set controllers. As you probably um a quick show of hands who run into this particular problem that you're rolling a new pot new uh stateful set and if one of the pots will fail the entire roll out will be stuck and the only reason to

### Excerpt da transcript

Hi everyone, thanks for coming to the saps talk. Today we're going to talk about managing data at scale best practices and evolution of sik apps. So what is sik apps? We focus on application user experience including the experience for app developers and app operators. We own the core workloads API including the deployment stateful set demon set job and chron job. We also help developing the application level tools and standards and for example the tools like helm and c uh c compose that some of you may have heard is under sig apps. We also sponsor some working group uh like batch working group and serving working group and this is the chairs of sigaps. I'm Janet. >> My name is Mache >> and then Ken Owens is not here um but maybe we'll see him in the future CubeCons. And this is our uh contact the bi-weekly we have bi-weekly meeting every Monday and then we also have the Slack channel and feel free to find us there. Now let's talk about a bunch of uh new features in this year. This is the um max unavailable for staple set.

This feature mainly focused on uh making the roll out uh faster so that we can improve the update speed and u flexibility while still maintaining the uh controller availability. With that I'm going to hand over to Mach. Um one one tiny little comment I would like to help uh shout out to Hiba for this particular work. Uh because um as you probably noticed a lot of the work that we do and the Kubernetes enhancements proposals the cap they the majority of them have fourdigit number. uh if you look carefully this one is threedigit one which means it goes back way way way too much in the past like if I remember correctly somewhere around 2018 so if you do the math quickly it's like seven years and the works um we were really struggling to get people to help us with the work there's only a handful of us who are working on the controllers and yet at the same time all of you and all of us rely rely on the core controllers and so changing them is not that simple thing and I'll be talking about because I have one specific use case and I know that Philip is already looking at me uh because he knows what I'm going to be talking about.

Um Janet covered the batch uh sorry the beta features that we promoted literally this current release that is going to be out there early December or late November I can't remember the exact date for 135 release but we're very happy and again big shout out to Heba uh for her work and involvement in that particular on
