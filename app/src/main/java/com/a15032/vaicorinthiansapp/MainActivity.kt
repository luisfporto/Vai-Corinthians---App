package com.a15032.vaicorinthiansapp

import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.LinearLayout
import android.widget.TextView
import android.widget.ImageView
import android.view.Gravity
import android.graphics.Color
import android.graphics.Typeface
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.cardview.widget.CardView
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import com.google.android.material.bottomnavigation.BottomNavigationView
import com.bumptech.glide.Glide

data class Player(
    val name: String,
    val age: Int,
    val height: String,
    val nationality: String,
    val position: String,
    val goals: Int,
    val lastClub: String,
    val imageUrl: String
)

class MainActivity : AppCompatActivity() {
    private lateinit var viewHome: View
    private lateinit var viewSquad: View
    private lateinit var viewTrivia: View
    private lateinit var viewTitles: View
    private lateinit var viewPlayerDetail: View

    private val squadList = listOf(
        Player("Hugo Souza", 25, "1.96m", "Brasil", "Goleiro", 0, "Flamengo", "https://img.a.transfermarkt.technology/portrait/medium/574901-1758160198.jpg?lm=1"),
        Player("Matheus Donelli", 21, "1.89m", "Brasil", "Goleiro", 0, "Base", "https://img.a.transfermarkt.technology/portrait/medium/708723-1725326064.jpg?lm=1"),
        Player("Fagner", 34, "1.68m", "Brasil", "Lateral Direito", 1, "VfL Wolfsburg", "https://upload.wikimedia.org/wikipedia/commons/e/e8/Paulist%C3%A3o_A1_-_S%C3%A3o_Bernardo_2x0_Corinthians_%2852681299548%29.jpg"),
        Player("Matheuzinho", 23, "1.71m", "Brasil", "Lateral Direito", 0, "Flamengo", "https://img.a.transfermarkt.technology/portrait/medium/594226-1725325967.jpg?lm=1"),
        Player("Hugo", 26, "1.78m", "Brasil", "Lateral Esquerdo", 0, "Goiás", "https://img.a.transfermarkt.technology/portrait/medium/730708-1700062381.jpg?lm=1"),
        Player("Matheus Bidu", 24, "1.72m", "Brasil", "Lateral Esquerdo", 0, "Cruzeiro", "https://img.a.transfermarkt.technology/portrait/medium/670021-1660574686.jpg?lm=1"),
        Player("André Ramalho", 32, "1.82m", "Brasil", "Zagueiro", 0, "PSV Eindhoven", "https://img.a.transfermarkt.technology/portrait/medium/175792-1721347430.jpg?lm=1"),
        Player("Félix Torres", 27, "1.87m", "Equador", "Zagueiro", 0, "Santos Laguna", "https://upload.wikimedia.org/wikipedia/commons/8/89/Felix_Torres_em_a%C3%A7%C3%A3o_pela_sele%C3%A7%C3%A3o_equatoriana_em_2021.png"),
        Player("Gustavo Henrique", 31, "1.96m", "Brasil", "Zagueiro", 0, "Valladolid", "https://img.a.transfermarkt.technology/portrait/medium/208681-1725326922.jpg?lm=1"),
        Player("Cacá", 24, "1.87m", "Brasil", "Zagueiro", 0, "Athletico-PR", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Caca_em_a%C3%A7%C3%A3o_pelo_Cruzeiro_em_2020.jpg/640px-Caca_em_a%C3%A7%C3%A3o_pelo_Cruzeiro_em_2020.jpg"),
        Player("Raniele", 27, "1.84m", "Brasil", "Volante", 0, "Cuiabá", "https://img.a.transfermarkt.technology/portrait/medium/546530-1680488285.jpg?lm=1"),
        Player("José Martínez", 29, "1.76m", "Venezuela", "Volante", 0, "Philadelphia Union", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Jose_Martinez_Philly.jpg/640px-Jose_Martinez_Philly.jpg"),
        Player("Charles", 27, "1.87m", "Brasil", "Volante", 0, "Midtjylland", "https://img.a.transfermarkt.technology/portrait/medium/486078-1771002454.jpg?lm=1"),
        Player("Alex Santana", 28, "1.82m", "Brasil", "Volante", 0, "Athletico-PR", "https://img.a.transfermarkt.technology/portrait/medium/219835-1622913468.png?lm=1"),
        Player("Breno Bidon", 19, "1.75m", "Brasil", "Meia", 0, "Base", "https://img.a.transfermarkt.technology/portrait/medium/1029227-1725327135.jpg?lm=1"),
        Player("Rodrigo Garro", 26, "1.74m", "Argentina", "Meia", 4, "Talleres", "https://img.a.transfermarkt.technology/portrait/medium/565009-1725327608.jpg?lm=1"),
        Player("Igor Coronado", 31, "1.70m", "Brasil", "Meia", 0, "Al-Ittihad", "https://upload.wikimedia.org/wikipedia/commons/a/a9/Coronado_in_the_Al-Ittihad_club_match.jpg"),
        Player("Yuri Alberto", 23, "1.83m", "Brasil", "Atacante", 8, "Zenit", "https://img.a.transfermarkt.technology/portrait/medium/489893-1744075236.jpg?lm=1"),
        Player("Memphis Depay", 30, "1.76m", "Holanda", "Atacante", 0, "Atlético de Madrid", "https://img.a.transfermarkt.technology/portrait/medium/167850-1668167349.jpg?lm=1"),
        Player("Ángel Romero", 31, "1.77m", "Paraguai", "Atacante", 0, "Cruz Azul", "https://upload.wikimedia.org/wikipedia/commons/1/12/%C3%81ngel_Romero_-_Sulamericana_CUP_2023_Semifinal_-_Corinthians_x_Fortaleza-CE_%2853554974439%29_%28cropped%29.jpg"),
        Player("Talles Magno", 21, "1.86m", "Brasil", "Atacante", 0, "New York City FC", "https://upload.wikimedia.org/wikipedia/commons/6/61/CINvNYC_2022-06-29_-_Maxime_Chanot%2C_Tayvon_Gray%2C_Talles_Magno%2C_Gabriel_Pereira%2C_Maxi_Moralez_%2852187858080%29_%28Magno_crop%29.jpg"),
        Player("Pedro Henrique", 33, "1.81m", "Brasil", "Atacante", 0, "Internacional", "https://upload.wikimedia.org/wikipedia/commons/1/1e/Pedro_Henrique_A_Kayserispor_2020.jpg")
    )

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, 0)
            insets
        }

        viewHome = findViewById(R.id.view_home)
        viewSquad = findViewById(R.id.view_squad)
        viewTrivia = findViewById(R.id.view_trivia)
        viewTitles = findViewById(R.id.view_titles)
        viewPlayerDetail = findViewById(R.id.view_player_detail)

        val squadContainer = findViewById<LinearLayout>(R.id.squad_container)
        populateSquad(squadContainer)

        val btnBackSquad = findViewById<Button>(R.id.btn_back_squad)
        btnBackSquad.setOnClickListener {
            viewPlayerDetail.visibility = View.GONE
        }

        val bottomNav = findViewById<BottomNavigationView>(R.id.bottom_navigation)
        bottomNav.setOnItemSelectedListener { item ->
            hideAllViews()
            viewPlayerDetail.visibility = View.GONE
            when (item.itemId) {
                R.id.nav_home -> {
                    viewHome.visibility = View.VISIBLE
                    true
                }
                R.id.nav_squad -> {
                    viewSquad.visibility = View.VISIBLE
                    true
                }
                R.id.nav_trivia -> {
                    viewTrivia.visibility = View.VISIBLE
                    true
                }
                R.id.nav_titles -> {
                    viewTitles.visibility = View.VISIBLE
                    true
                }
                else -> false
            }
        }
    }

    private fun populateSquad(container: LinearLayout) {
        val density = resources.displayMetrics.density
        for (player in squadList) {
            val card = CardView(this).apply {
                layoutParams = LinearLayout.LayoutParams(
                    LinearLayout.LayoutParams.MATCH_PARENT,
                    LinearLayout.LayoutParams.WRAP_CONTENT
                ).apply {
                    setMargins(0, 0, 0, (12 * density).toInt())
                }
                radius = 12 * density
                setCardBackgroundColor(Color.parseColor("#222222"))
                elevation = 4 * density
                isClickable = true
                isFocusable = true
                setOnClickListener {
                    showPlayer(player)
                }
            }

            val cardContent = LinearLayout(this).apply {
                orientation = LinearLayout.HORIZONTAL
                setPadding((16 * density).toInt(), (16 * density).toInt(), (16 * density).toInt(), (16 * density).toInt())
                gravity = Gravity.CENTER_VERTICAL
            }

            val imageView = ImageView(this).apply {
                layoutParams = LinearLayout.LayoutParams(
                    (60 * density).toInt(),
                    (60 * density).toInt()
                ).apply {
                    setMargins(0, 0, (16 * density).toInt(), 0)
                }
                scaleType = ImageView.ScaleType.CENTER_CROP
            }

            Glide.with(this)
                .load(player.imageUrl)
                .circleCrop()
                .into(imageView)

            val textLayout = LinearLayout(this).apply {
                orientation = LinearLayout.VERTICAL
            }

            val tvName = TextView(this).apply {
                text = player.name
                textSize = 20f
                setTextColor(Color.WHITE)
                setTypeface(null, Typeface.BOLD)
            }

            val tvPos = TextView(this).apply {
                text = player.position
                textSize = 16f
                setTextColor(Color.parseColor("#CCCCCC"))
            }

            textLayout.addView(tvName)
            textLayout.addView(tvPos)

            cardContent.addView(imageView)
            cardContent.addView(textLayout)
            card.addView(cardContent)
            container.addView(card)
        }
    }

    private fun showPlayer(player: Player) {
        findViewById<TextView>(R.id.detail_player_name).text = player.name
        findViewById<TextView>(R.id.detail_player_position).text = player.position
        findViewById<TextView>(R.id.detail_age).text = "Idade: ${player.age}"
        findViewById<TextView>(R.id.detail_height).text = "Altura: ${player.height}"
        findViewById<TextView>(R.id.detail_nationality).text = "Nacionalidade: ${player.nationality}"
        findViewById<TextView>(R.id.detail_goals).text = "Gols nesta temporada: ${player.goals}"
        findViewById<TextView>(R.id.detail_last_club).text = "Último Clube: ${player.lastClub}"
        
        // Also add the photo to the detail view if there's an ImageView for it. 
        // We'll peek if an imageView is there, if we modify the layout later.
        val detailPhoto = findViewById<ImageView>(R.id.detail_player_photo)
        if (detailPhoto != null) {
            Glide.with(this)
                .load(player.imageUrl)
                .circleCrop()
                .into(detailPhoto)
        }
        
        viewPlayerDetail.visibility = View.VISIBLE
    }

    private fun hideAllViews() {
        viewHome.visibility = View.GONE
        viewSquad.visibility = View.GONE
        viewTrivia.visibility = View.GONE
        viewTitles.visibility = View.GONE
    }
}