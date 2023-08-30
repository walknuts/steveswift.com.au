defmodule GumroadDownloader do

  require Jason
  require Slug

  def get_json(filename) do
    with {:ok, body} <- File.read(filename),
         {:ok, json} <- Jason.decode(body, keys: :atoms), do: {:ok, json}
  end

  def item_to_html(%{name: name, preview_url: _image_url, description: description, file_info: info}) do
    image_filename = Slug.slugify(name) <> ".jpg"
    # {_, 0} = System.cmd("curl", [image_url, "-o", image_filename])

    """
    <article class="entry">
    <img style="width: 100%; height:56.25%; object-size: cover;" src="{% link assets/images/papers/#{image_filename} %}">
    <h2>#{name}</h2>
    <p>#{info[:Length]} (#{info[:Size]})</p>
    #{description}
    </article>

    """
  end

  def main do
    {:ok, data} = get_json("../../../_data/gumroad.json")

    output =
      data
      |> Enum.map(&item_to_html/1)

    File.write!("cards.html", output)
  end
end

GumroadDownloader.main
