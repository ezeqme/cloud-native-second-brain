---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2024"
edition_id: 2024-berlin
year: 2024
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Kubernetes", "Scalability Reliability"]
speakers: ["M Viswanath Sai", "S Ashwin"]
source_url: https://promcon.io/2024-berlin/talks/harnessing-the-potential-of-prometheus-agent-mode/
youtube_url: https://www.youtube.com/watch?v=wkkXh8X0N8s
youtube_search_url: https://www.youtube.com/results?search_query=Harnessing+the+potential+of+Prometheus+Agent+mode+PromCon+2024
video_match_score: 1.013
status: video-found
---

# Harnessing the potential of Prometheus Agent mode

## Identificação

- Edição: PromCon EU 2024
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Kubernetes]], [[Scalability Reliability]]
- Speakers: M Viswanath Sai, S Ashwin
- Página oficial: https://promcon.io/2024-berlin/talks/harnessing-the-potential-of-prometheus-agent-mode/
- YouTube: https://www.youtube.com/watch?v=wkkXh8X0N8s

## Resumo

We already have a lot of Prometheus Agent mode "StatefulSet vs DaemonSet deployment model" comparisons, ironically however, choosing between StatefulSet and DaemonSet models can be quite confusing due to the lack of solid, data-backed advice. Our session aims to clear the air around this situation by providing practical, data backed insights based on real-world scenarios. We'll share empirical findings that show where each deployment model shines, where they are not advisable to use etc., so that the audience can make informed decisions.

## Abstract oficial

We already have a lot of Prometheus Agent mode "StatefulSet vs DaemonSet deployment model" comparisons, ironically however, choosing between StatefulSet and DaemonSet models can be quite confusing due to the lack of solid, data-backed advice. Our session aims to clear the air around this situation by providing practical, data backed insights based on real-world scenarios.

We'll share empirical findings that show where each deployment model shines, where they are not advisable to use etc., so that the audience can make informed decisions. We will also explore "hybrid deployment" approaches that combine both models, something that is being experimented with, at Prometheus-Operator. This offers new ways to scale and ensure reliability—an approach not widely discussed.

Alongside practical tips, we'll narrate the story of how Agent mode came to be, it's raise to monitoring stardom, and how it has evolved to meet different operational needs.

Join us for a straightforward and engaging session that combines real data with a compelling narrative, giving you practical takeaways and a deeper understanding of Prometheus Agent deployments.

## Links

- Página oficial: https://promcon.io/2024-berlin/talks/harnessing-the-potential-of-prometheus-agent-mode/
- YouTube: https://www.youtube.com/watch?v=wkkXh8X0N8s
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=wkkXh8X0N8s
- YouTube title: PromCon 2024 - Harnessing the Potential of Prometheus Agent Mode
- Match score: 1.013
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2024/harnessing-the-potential-of-prometheus-agent-mode/wkkXh8X0N8s.txt
- Transcript chars: 24240
- Keywords: server, metrics, scrape, cluster, operator, pretty, running, questions, scraping, resource, question, possible, stateful, little, compared, visibility, reliability, monitoring

### Resumo baseado na transcript

[Music] [Applause] yeah so good to see you all yeah first time here so it's a huge honor for us coming here like in our University our exams are going on we skipped it to be here so I hope no one sees us on YouTube or something yeah yeah yep hey everyone um the blog we have for you here today is the byproduct of a lot of discussions we've had over at prome operator um about we recently started implementing the Damon set model for the promes agent

### Excerpt da transcript

[Music] [Applause] yeah so good to see you all yeah first time here so it's a huge honor for us coming here like in our University our exams are going on we skipped it to be here so I hope no one sees us on YouTube or something yeah yeah yep hey everyone um the blog we have for you here today is the byproduct of a lot of discussions we've had over at prome operator um about we recently started implementing the Damon set model for the promes agent and this is the byproduct of those discussions so just a quick introduction I am Vish sa Mutu you can call me vishwa I a contributor and g m at pritus operator I worked at on extending the this C called Script config um we're hoping to you know promote it to Beta unstable soon and uh I'm a final year engineering undergrad at the Indian Institute of Technology Varanasi um my hobbies I love to play football badminton Cricket I play a lot of sports and uh I love dogs yeah yeah I am shiram aswin you can call me Ashan so yeah I also worked like him as a g mentee at pus operator I worked mainly on documentation website and now after completing my G project I'm now the maintainer in that website repo I'm also finally year student at itbu like him and yeah my hobbies I like singing even listening to music and loves doing sports we both play football together yeah uh just a quick show of hands yeah so how many of you use prom's agent all right good nice and how many of you use promise's operator yeah okay that's nice there's a lot of people yeah so this talk is more of kind of a story that we W around it's an imaginary story so let's get into it so we will talk about a farmer named daa she she's a very futuristic kind of thinking so yeah she uses tools like iot devices BS to monitor field she collects data using mon monitoring tools like Prometheus so yeah she likes to do stuff analyze the data to a lab that is her main priority to improve yeah we totally did not rip this off from Arthur and Nicholas uh so Eva has uh two Farms two and to make it easier for us uh we call each Farms a cluster and each acre of land in the farm will be called a node and each individual iot device will be be a PO from where we get collect metrics using her Prometheus server with a ha pair each of her clusters right so that's what she does she collects metrics from her farms and sends it over the wire to a lab to analyze and improve her productivity I mean but there are every time there are some downsides and when she look at her expenses the mo
