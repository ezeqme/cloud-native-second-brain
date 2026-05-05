---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Observability"
themes: ["Observability"]
speakers: ["Kruthika Prasanna Simha", "Raj Bhensadadia", "Apple Inc."]
sched_url: https://kccncna2024.sched.com/event/1i7pF/now-you-see-me-tame-mttr-with-real-time-anomaly-detection-kruthika-prasanna-simha-raj-bhensadadia-apple-inc
youtube_search_url: https://www.youtube.com/results?search_query=Now+You+See+Me%3A+Tame+MTTR+with+Real-Time+Anomaly+Detection+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Now You See Me: Tame MTTR with Real-Time Anomaly Detection - Kruthika Prasanna Simha & Raj Bhensadadia, Apple Inc.

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United States / Salt Lake City
- Speakers: Kruthika Prasanna Simha, Raj Bhensadadia, Apple Inc.
- Schedule: https://kccncna2024.sched.com/event/1i7pF/now-you-see-me-tame-mttr-with-real-time-anomaly-detection-kruthika-prasanna-simha-raj-bhensadadia-apple-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Now+You+See+Me%3A+Tame+MTTR+with+Real-Time+Anomaly+Detection+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Now You See Me: Tame MTTR with Real-Time Anomaly Detection.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7pF/now-you-see-me-tame-mttr-with-real-time-anomaly-detection-kruthika-prasanna-simha-raj-bhensadadia-apple-inc
- YouTube search: https://www.youtube.com/results?search_query=Now+You+See+Me%3A+Tame+MTTR+with+Real-Time+Anomaly+Detection+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Ipc0SOhB9OM
- YouTube title: Now You See Me: Tame MTTR with Real-Time Anomaly Dete... Kruthika Prasanna Simha & Prschita Prschita
- Match score: 0.808
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/now-you-see-me-tame-mttr-with-real-time-anomaly-detection/Ipc0SOhB9OM.txt
- Transcript chars: 33492
- Keywords: detection, anomaly, anomal, meantime, analysis, actually, metrics, models, detect, question, learning, machine, dependency, identification, methods, features, specific, causes

### Resumo baseado na transcript

um good evening everyone uh thank you for being here so late this evening and I promise you I won't keep you all for too long from your um dinner plans so today what we want to talk about is how you can use your anomaly detection methods and enhance them to impact meantime to respond so without further Ado let's Jump Right In so we'll take a quick moment to introduce ourselves um if any of you attended my talk yesterday um you'll remember me I'm cria um I'm

### Excerpt da transcript

um good evening everyone uh thank you for being here so late this evening and I promise you I won't keep you all for too long from your um dinner plans so today what we want to talk about is how you can use your anomaly detection methods and enhance them to impact meantime to respond so without further Ado let's Jump Right In so we'll take a quick moment to introduce ourselves um if any of you attended my talk yesterday um you'll remember me I'm cria um I'm a machine learning engineer at Apple and I work in the observability team my background is in observability machine learning and data science um prita hi I'm prita I an engineering manager at Apple I lead our observability Intelligence and Analysis team and my background is an observable team machine learning data science and data engineering all righty so um let's do a quick walk through of our um agenda for today so we're going to start with a case study um talk about what is the problem with delayed detection and then how normally detection can help with that and reduce meantime to detect and then we'll jump into um you know a little more advanced uh anomal detection methods that can help with root cause detection and how that reduces mttr and finally we'll jump into some questions okay so for most of us here when we say anomaly detection we automatically associate that with mean time to detect however you can enhance your anomaly detection methods and add some contextual information to it to get a lot more insights from anomaly detection and so the core focus of our talk today is going to be how you can leverage realtime anomal detection methods to not just improve meantime to detect but also improve meantime to resolve um some of the key takeaways we hope you'll get today is we'll talk a little bit about value proposition of anomal detection talk about some of the statistical and machine learning methods that are out there for anomally detection and then jump into the important part which is how can you improve meantime to resolve with anomal detection and also talk about how you can leverage some of the open- source um Frameworks and tools to build your anomaly detection pipeline so with that rashita do you want to take away with our use case thank you cria all right so we'll start by setting up some context for our case study imagine that you creating your very first online service which is an astronomy shop sounds really cool it is it is every space Explorer dream it's full of all these fancy ga
