use Baocao
CREATE TABLE Account (
    UserID INT PRIMARY KEY IDENTITY(1,1),
    Username NVARCHAR(50) UNIQUE,
    Password NVARCHAR(100),
	TrangThai bit
)
CREATE TABLE Quanly (
    Masach INT PRIMARY KEY IDENTITY(1,1),
    Tensach NVARCHAR(50)FOREIGN KEY REFERENCES Muonvatra(Tensach),
    Soluong INT,
    Nxb NVARCHAR(50),
    Tacgia NVARCHAR(50)
);

CREATE TABLE Muonvatra (
    ID INT PRIMARY KEY IDENTITY(1,1),
    Tennguoimuon NVARCHAR(50),
    Masach INT FOREIGN KEY REFERENCES Quanly(Masach),
	Tensach nvarchar (50) FOREIGN KEY REFERENCES Quanly(Tensach),
    Soluong INT,
    NgayMuon varchar(20),
    NgayTra varchar(20),
	Lienhe nvarchar(50) null
);
CREATE TABLE Thongke(
	Ngaymuon Nvarchar(50) PRIMARY KEY IDENTITY(1,1),
	Ngaytra Nvarchar(50),
)
-- Thêm dữ liệu vào Account
INSERT INTO Account (Username, Password, TrangThai) VALUES
('user1', 'password1', 1),
('user2', 'password2', 1),
('user3', 'password3', 0),
('user4', 'password4', 1),
('user5', 'password5', 0);

-- Thêm dữ liệu vào Quanly
INSERT INTO Quanly (Tensach, Soluong, Nxb, Tacgia) VALUES
(N'Sách A', 10, N'NXB Kim Đồng', N'Tác giả A'),
(N'Sách B', 5, N'NXB Trẻ', N'Tác giả B'),
(N'Sách C', 20, N'NXB Giáo Dục', N'Tác giả C'),
(N'Sách D', 15, N'NXB Văn Học', N'Tác giả D'),
(N'Sách E', 8, N'NXB Chính Trị', N'Tác giả E');

-- Thêm dữ liệu vào Muonvatra
INSERT INTO Muonvatra (Tennguoimuon, Masach, Tensach, Soluong, NgayMuon, NgayTra) VALUES
(N'Nguyễn Văn A', 1,N'Sách E', 2, '2024-12-01', '2024-12-10'),
(N'Trần Thị B', 2, N'Sách D', 1, '2024-12-02', '2024-12-11'),
(N'Lê Văn C', 3, N'Sách C', 3, '2024-12-03', '2024-12-12'),
(N'Phạm Văn D', 4, N'Sách B', 1, '2024-12-04', '2024-12-13'),
(N'Hoàng Thị E', 5,N'Sách A', 2, '2024-12-05', '2024-12-14');

SELECT ID FROM Muonvatra WHERE ID = 2