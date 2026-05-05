---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Security"
themes: ["AI ML", "Security"]
speakers: ["Erica Hughberg", "Tetrate", "Andres Aguiar", "Okta"]
sched_url: https://kccnceu2026.sched.com/event/2CW6G/tailor-made-dynamic-fine-grained-authorization-for-api-traffic-erica-hughberg-tetrate-andres-aguiar-okta
youtube_search_url: https://www.youtube.com/results?search_query=Tailor+Made%3A+Dynamic+Fine-Grained+Authorization+for+API+Traffic+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Tailor Made: Dynamic Fine-Grained Authorization for API Traffic - Erica Hughberg, Tetrate & Andres Aguiar, Okta

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Erica Hughberg, Tetrate, Andres Aguiar, Okta
- Schedule: https://kccnceu2026.sched.com/event/2CW6G/tailor-made-dynamic-fine-grained-authorization-for-api-traffic-erica-hughberg-tetrate-andres-aguiar-okta
- Busca YouTube: https://www.youtube.com/results?search_query=Tailor+Made%3A+Dynamic+Fine-Grained+Authorization+for+API+Traffic+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Tailor Made: Dynamic Fine-Grained Authorization for API Traffic.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW6G/tailor-made-dynamic-fine-grained-authorization-for-api-traffic-erica-hughberg-tetrate-andres-aguiar-okta
- YouTube search: https://www.youtube.com/results?search_query=Tailor+Made%3A+Dynamic+Fine-Grained+Authorization+for+API+Traffic+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=A1FXOwUmA6M
- YouTube title: Tailor Made: Dynamic Fine-Grained Authorization for API Traffic - Erica Hughberg & Andres Aguiar
- Match score: 0.89
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/tailor-made-dynamic-fine-grained-authorization-for-api-traffic/A1FXOwUmA6M.txt
- Transcript chars: 25360
- Keywords: access, envoy, gateway, actually, authorization, specific, engineering, resource, request, dynamic, interesting, important, permissions, exciting, simple, complicated, traffic, together

### Resumo baseado na transcript

And this is uh to me quite exciting because for me this presentation is putting two of my most wonderful things together because I happen to have dealt with a lot of API traffic in my career and uh I thought security and authorization was one of the hardest thing ever which is kind of the opposite to you maybe. And I remember when I got my head around OAF, it still had some challenges that it wasn't really solving for me because for example, I worked in fintech for a while and people were like, well, if we remove access to a portfolio, we want them to not have access to the portfolio straight away. >> They all talk about authorization, but like it needs to be fast as well because one of the challenges that I had, right? this is my favorite architecture diagram Andress my favorite one because we're all drawn it. So it you kind of have to make three API calls to different services to know if the user can access this specific resource right you want to do something that is very quickly and uh they can scale and those kind of things >> And and because I am a big fan of authorization we actually made it super easy in on gateway like with a kubernetes uh cd there that you can actually define the coarse grain stuff super easy but it does not solve the fine grain problem because it gets static and yeah so what are we doing?

### Excerpt da transcript

And this is uh to me quite exciting because for me this presentation is putting two of my most wonderful things together because I happen to have dealt with a lot of API traffic in my career and uh I thought security and authorization was one of the hardest thing ever which is kind of the opposite to you maybe. >> I don't know I tried to been trying to fix that for a while. I don't know if we succeeded but keep trying. >> Yeah. And I remember when I got my head around OAF, it still had some challenges that it wasn't really solving for me because for example, I worked in fintech for a while and people were like, well, if we remove access to a portfolio, we want them to not have access to the portfolio straight away. And I'm like, ah, okay. So, I can't really bake that in to the token because if I did, then we have to wait for the token to expire. We have to have like back. It was a lot of mess. >> Yeah. >> And the good news is that you see your boss asks you this. Wonderful question. >> So, and is your boss texting through iMessage?

>> Yeah. >> Interesting. >> That's got a Slack message overnight, but not that iMessage. >> And now, you know, when it's important, you get iMessage. >> Yeah. If you work in fintech, fintech is more pressing, I guess. Yeah. >> It's like got to get it sorted now. So the challenge here that I've had to deal with multiple times is want to both protect internal resources also as well as external because sometimes we route API traffic to resources we do not control. Um but we want to protect those internal apps and we make those this is the hard part make the authorization changes take effect immediately. >> Yeah. >> Right. >> So >> looks hard >> looks hard. I I think I think you might have a solution up your back pocket, Andress. I think we're gonna be fine. You You forgot it. You didn't bring it. Andreas, I told you to prepare. >> You should make a ticket. >> Make a ticket. Yeah, cuz he >> and I message to someone to get ready. >> So, what are we really dealing with here? What does the environment look like? So, the thing is the first time I dealt with this problem, there were no agents hanging around.

They've come along now, but actually they're not that awfully much different. But we had a lot of application like server side apps making requests. >> I wonder why we keep using that kind of smiley thing for Asians because they're looking more scary. >> You think they're scary? >> Yeah. >> Right. So they can do crazy things. I don
