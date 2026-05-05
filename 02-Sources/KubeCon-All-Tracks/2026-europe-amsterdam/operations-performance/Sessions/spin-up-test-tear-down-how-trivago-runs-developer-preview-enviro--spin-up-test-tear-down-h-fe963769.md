---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Operations + Performance"
themes: ["SRE Reliability"]
speakers: ["Armin Aminian", "Trivago", "Jan Wozniak", "Kedify"]
sched_url: https://kccnceu2026.sched.com/event/2CW6Y/spin-up-test-tear-down-how-trivago-runs-developer-preview-environments-at-scale-armin-aminian-trivago-jan-wozniak-kedify
youtube_search_url: https://www.youtube.com/results?search_query=Spin-Up%2C+Test%2C+Tear-Down%3A+How+Trivago+Runs+Developer+Preview+Environments+at+Scale+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Spin-Up, Test, Tear-Down: How Trivago Runs Developer Preview Environments at Scale - Armin Aminian, Trivago & Jan Wozniak, Kedify

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Operations + Performance]]
- Temas: [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Armin Aminian, Trivago, Jan Wozniak, Kedify
- Schedule: https://kccnceu2026.sched.com/event/2CW6Y/spin-up-test-tear-down-how-trivago-runs-developer-preview-environments-at-scale-armin-aminian-trivago-jan-wozniak-kedify
- Busca YouTube: https://www.youtube.com/results?search_query=Spin-Up%2C+Test%2C+Tear-Down%3A+How+Trivago+Runs+Developer+Preview+Environments+at+Scale+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Spin-Up, Test, Tear-Down: How Trivago Runs Developer Preview Environments at Scale.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW6Y/spin-up-test-tear-down-how-trivago-runs-developer-preview-environments-at-scale-armin-aminian-trivago-jan-wozniak-kedify
- YouTube search: https://www.youtube.com/results?search_query=Spin-Up%2C+Test%2C+Tear-Down%3A+How+Trivago+Runs+Developer+Preview+Environments+at+Scale+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_stuEBA4nK0
- YouTube title: Spin-Up, Test, Tear-Down: How Trivago Runs Developer Preview Environm... Armin Aminian & Jan Wozniak
- Match score: 0.899
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/spin-up-test-tear-down-how-trivago-runs-developer-preview-environments/_stuEBA4nK0.txt
- Transcript chars: 27197
- Keywords: preview, environment, request, application, production, add-on, github, second, everything, feature, scaled, object, interceptor, engineer, scaling, booking, staging, deploy

### Resumo baseado na transcript

>> So yeah uh today we are going to talk about how Tivago runs developer preview environment u at the scale. Uh so how many of you have used uh tiago to like find the accommodation? But if you have like a scale of tuago with 200 developers so they need to wait for a staging to be free or the test would be unreliable because Jan can create a PR and then it affect my change or I can blame him. So we had our front- end application on uh GCP cloud run and the GCP cloud run is like a serverless container platform that lets you to deploy containers without any you know pain of ISO uh and u so and it also supports a scale to zero and we had our backend services uh on GKE sorry there go I'm finally really useful. Kubernetes and of course we had to uh maintain two split architecture of uh monitoring logging deployment which was very painful but was was very good for our preview environment because we could handle more than 600 uh front end preview with just 100 euro So our strategy was to unify everything on Kubernetes but how to keep cheap preview environment.

### Excerpt da transcript

Welcome to our presentation. Uh I'm Armen. I'm S at Tago >> and my name is Jan and I'm a maintainer. >> So yeah uh today we are going to talk about how Tivago runs developer preview environment u at the scale. So yeah let's get started. Uh so how many of you have used uh tiago to like find the accommodation? Okay. Okay. Not bad. I expect more hands from my colleague. So it would be affect your salary soon. Uh so uh so >> by the way talking about your colleagues, have you used Tago to book your recommendations? >> Uh no. Uh so yeah uh Triago we are a travel meta search engine uh that compare accommodation pro prices across multiple OTAs. So it could be booking.com, Expedia and our goal is to help the user to find the best uh deal and you might have heard uh hotel tiago thousand times uh in from our uh TV ads. So uh Tivago infrastructure so we have more than 100 microservices. We deployed those uh across uh three region to give a better user experience and latency and everything uh is running on GKE Kubernetes uh cluster.

Uh so when you suppose you Jan opens Tago or our application he search for accommodation what would be happen? So the request uh some requests will be uh fired against our graphare router and our graphare router responsible to send or fan out uh those to our subgraph and those subgraph are uh going to you know find prices accommodation details from our search and the price uh infrastructure which are connected to uh OTAAS. So what is the preview environment exactly? Let's follow uh Alex journey. So Alex he's one of our lovely uh developer he's working on uh one of our important services so imaginary service here so booking service and he needs to add a new feature to this uh booking service and this booking service also has a dependency to both search service and the payment service. So test pass, everything looks perfect on Alex machine and he said, "Yeah, it works on my machine." It's like a f famous word of engineer before introducing a big incident. And but will it work in production with the real dependency uh that we have on our staging or on our production?

>> I I think I'm not going to give away a secret, but it didn't. >> It didn't. He merged it. He introduced a incident uh SR pissed 100k u lost. So what doesn't work? So in the traditional approach if you want to ship something on a production into the production you can say I would test it on my local it would work but the local completely is completely different than production
