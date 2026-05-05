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
themes: ["AI ML", "Networking", "Community Governance"]
speakers: ["James Strong", "Chainguard", "Ricardo Katz", "VMware"]
sched_url: https://kccncna2022.sched.com/event/18lgl/understanding-the-future-of-ingress-nginx-james-strong-chainguard-ricardo-katz-vmware
youtube_search_url: https://www.youtube.com/results?search_query=Understanding+the+Future+of+Ingress-nginx+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Understanding the Future of Ingress-nginx - James Strong, Chainguard & Ricardo Katz, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Networking]], [[Community Governance]]
- País/cidade: United States / Detroit
- Speakers: James Strong, Chainguard, Ricardo Katz, VMware
- Schedule: https://kccncna2022.sched.com/event/18lgl/understanding-the-future-of-ingress-nginx-james-strong-chainguard-ricardo-katz-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=Understanding+the+Future+of+Ingress-nginx+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Understanding the Future of Ingress-nginx.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/18lgl/understanding-the-future-of-ingress-nginx-james-strong-chainguard-ricardo-katz-vmware
- YouTube search: https://www.youtube.com/results?search_query=Understanding+the+Future+of+Ingress-nginx+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=bkLLpPc0f7E
- YouTube title: Understanding the Future of Ingress-nginx - James Strong, Chainguard & Ricardo Katz, VMware
- Match score: 0.731
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/understanding-the-future-of-ingress-nginx/bkLLpPc0f7E.txt
- Transcript chars: 33395
- Keywords: ingress, working, actually, support, gateway, questions, little, trying, looking, probably, security, release, survey, issues, understand, version, control, maintain

### Resumo baseado na transcript

we're going to do an uh unsanctioned karaoke session hello everyone my name is James strong I don't think it's moderated so we can just get started yeah yeah we can awesome I I will self moderate us gotcha Welcome to our comedy session thank you open mic no I make jokes when I'm nervous so uh be prepared hello everyone my name is James strong I'm a Solutions architect at changuard and what that means is I help people secure their software Supply chains um look at gaps of be supporting so if you have any feedback on that please let us know what versions of Ingress are currently running in production so of course we have Ingress versus versions of kubernetes really good so back when we put the survey out we were what that's 70 pull requests oh yeah um two other things I went to the tax security meeting yesterday we're gonna go work through the threat modeling and get that evaluated working through the project and understanding what else we can do to help secure is the one that actually implemented the all of the Lua stuff because in China X didn't support it hot reloads right so he solved a bunch of people problem with that because we are the the original reason that we move it to AJ yeah that's not that's good enough the if you purchase a support contract from nginx it's for the nginx Ingress controller yeah yeah so not the not not the open source yeah okay no problem we get...

### Excerpt da transcript

we're going to do an uh unsanctioned karaoke session hello everyone my name is James strong I don't think it's moderated so we can just get started yeah yeah we can awesome I I will self moderate us gotcha Welcome to our comedy session thank you open mic no I make jokes when I'm nervous so uh be prepared hello everyone my name is James strong I'm a Solutions architect at changuard and what that means is I help people secure their software Supply chains um look at gaps of those and uh and I also help maintain Ingress in genetics and I wrote a book about networking kubernetes but please don't ask me about your IP tables hey my name is Ricardo uh I am one of the maintainers as well I'm a software engineer at VMware so when I'm not creating books at Ingress in China next I'm creating books at VMware products So today we're gonna talk and uh we're gonna talk about understanding the future of Ingress nginx we're going to talk so we did a community survey probably about four or five months ago if you filled out that survey and you're here thank you very much we're going to talk about the stabilization project that we've been working on and we're going to do a little discussion about the road map some of this stuff some of the bugs that Ricardo's introducing and a little bit of q a if you have questions so uh this time is the community time so if you have questions for us um just go ahead and yell at us throw things Ricardo will catch them so I'm going to talk about the community survey results one of the first things we asked I thought was pretty obvious but I wanted to we wanted to understand what people were using and what they thought was most critical in Ingress engine X and uh that makes pretty that makes sense right load balancing and the fact that it was open source so um good to know that everyone's using it for what we intended to use it for but um we need to talk about that guy he's on our roadmap and for some of you who don't know mod security is being deprecated so I'm gonna have some work to figure that out versions of kubernetes um who's running anything older than 121.

I do for testing this is good um we wanted to put this out there because we again we wanted to understand what folks were using and when we talk about what's supported from our perspective it's looking at um the end-to-end tests that we run so you'll see that we run a lot of end-to-end tests they take about 45 minutes to run each time we have a PR so we want to make sure that those
