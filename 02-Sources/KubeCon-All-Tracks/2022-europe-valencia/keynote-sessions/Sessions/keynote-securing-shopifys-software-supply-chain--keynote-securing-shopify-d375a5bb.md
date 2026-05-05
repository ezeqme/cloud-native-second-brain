---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Keynote Sessions"
themes: ["AI ML", "Security"]
speakers: ["Shane Lawrence", "Staff Infrastructure Security Engineer", "Shopify"]
sched_url: https://kccnceu2022.sched.com/event/yuFX/keynote-securing-shopifys-software-supply-chain-shane-lawrence-staff-infrastructure-security-engineer-shopify
youtube_search_url: https://www.youtube.com/results?search_query=Keynote%3A+Securing+Shopify%27s+Software+Supply+Chain+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Keynote: Securing Shopify's Software Supply Chain - Shane Lawrence, Staff Infrastructure Security Engineer, Shopify

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]], [[Security]]
- País/cidade: Spain / Valencia
- Speakers: Shane Lawrence, Staff Infrastructure Security Engineer, Shopify
- Schedule: https://kccnceu2022.sched.com/event/yuFX/keynote-securing-shopifys-software-supply-chain-shane-lawrence-staff-infrastructure-security-engineer-shopify
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote%3A+Securing+Shopify%27s+Software+Supply+Chain+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Keynote: Securing Shopify's Software Supply Chain.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/yuFX/keynote-securing-shopifys-software-supply-chain-shane-lawrence-staff-infrastructure-security-engineer-shopify
- YouTube search: https://www.youtube.com/results?search_query=Keynote%3A+Securing+Shopify%27s+Software+Supply+Chain+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=yuDMsB0jsdE
- YouTube title: Keynote: Securing Shopify's Software Supply Chain - Shane Lawrence, Shopify
- Match score: 0.883
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/keynote-securing-shopifys-software-supply-chain/yuDMsB0jsdE.txt
- Transcript chars: 16051
- Keywords: supply, software, chains, little, toolbar, security, dependencies, information, systems, container, wanted, images, somebody, suspicious, exactly, vulnerability, working, securing

### Resumo baseado na transcript

good morning really excited to be here thank you all for coming i'm going to talk a little bit about securing software supply chains and i'm not the only person who's talking about this lately it seems to be an incredibly popular topic if any of you were here for the security conference on monday there were several talks about it and it's been coming up in the news more and more there's a lot of buzz around this and it's not surprising given how many attacks we've seen in

### Excerpt da transcript

good morning really excited to be here thank you all for coming i'm going to talk a little bit about securing software supply chains and i'm not the only person who's talking about this lately it seems to be an incredibly popular topic if any of you were here for the security conference on monday there were several talks about it and it's been coming up in the news more and more there's a lot of buzz around this and it's not surprising given how many attacks we've seen in the wild so rather than try to go over all the things that you can see in another talk or look up yourself i'm just going to give you a little bit of information very briefly about some of the challenges that my colleagues at shopify have run into with this some of the lessons that we've learned and why i think this is so important of course i'm most familiar with shopify's use case but we all share operating systems languages libraries and here in particular a container orchestrator so this is not a zero-sum game this is a collaborative effort i think the best time for all of this focus would have been 20 years ago before we built most of our infrastructure on a tangled web of hidden dependencies and unmeasured risk but the second best time is right now now it's been a long time since i got to come to kubecon in person but when i was preparing for this talk i was thinking back to my very first kubecon in 2017 and i knew that if i wanted to give a talk on container images i was going to need a lot of images of containers so i'd like to take the simple task of how i would find those images and use it to show a software engineering process it's not the waterfall with it don't worry so just like anything else that i might try to do when solving a problem i'm going to go out i'm going to look to see if somebody has already solved this problem for me and offered the solution for free so i plug in my ub key i fire up my work laptop and i get ready to yolo click some risky links let's filter for only top quality safe containers and if this isn't quite what we need we can scroll down oh this looks better it's a magic container image toolbar let's give it a whirl okay we can just download it there's not even a charge for it it's got great reviews there's no way that those could be fake now if it says it needs admin privileges that's probably fine right it makes sense it needs to administer all of those sweet container images so what do you think would you install this would you download this have
